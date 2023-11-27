from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView

from .models import Catalog, Book, Member
from .forms import CatalogForm, BookForm, CreateUserForm, MemberForm

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

from django.contrib.auth.mixins import LoginRequiredMixin


# HomePage 
def index(request):
    active_books = Book.objects.filter(is_active=True)
    print("Active Books available", active_books )
    return render(request, 'book_app/index.html', {'active_books':active_books})

#This will display only the catalogs of the signed in user
@login_required(login_url='login')
@allowed_users(allowed_roles=['Book Members'])
def catalogsView(request):
    member = request.user.member
    catalogs = member.members.all() if member.catalog else []
    context = {'catalogs': catalogs}
    return render(request, 'book_app/user_catalogs.html', context)

#List all available Catalogs
# Note: Since we have a generic List implemented, 
# it will automatically render a catalog_list.html that we need to create
class CatalogListView(LoginRequiredMixin, generic.ListView):
    model = Catalog

#List detail of catalog
class CatalogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Catalog

    #Get all books associated with that catalog 
    def get_context_data(self, **kwargs):
        #Call the base implmenatation first to get a context
        context = super().get_context_data(**kwargs)
        #Add in a QuerySet of all the projects
        context["books"] = Book.objects.filter(catalog=self.object)
        return context

#List all available books
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

#List the detail of that book 
class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'])
#Function that allows members to create a catalog 
def createCatalog(request):
    form = CatalogForm()

    if request.method == 'POST':
        #Create a dictonairy with the form data
        catalog_data = request.POST.copy()
        
        form = CatalogForm(catalog_data)
        #Checks to see if the form was filled out correctly
        if form.is_valid():
            #Get the current user
            user = request.user
            #Save the form 
            catalog = form.save(commit= False)
            #Associate the catalog with the current user
            catalog.member = user
            catalog.save()

            #Redirect back to catalog 
            return redirect('catalogs')
        
    context = {'form': form}
    return render(request, 'book_app/create_catalog.html', context)




#Restrict access to update catalogs if not logged in
@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'] )
#Class to update the Catalog
def updateCatalog(request, catalog_id):
    catalog = Catalog.objects.get(pk=catalog_id)
    form = CatalogForm(instance = catalog)

    if request.method == 'POST':
        #Create a dictonairy with the form data
        catalog_data = request.POST.copy()
        catalog_data['catalog_id'] = catalog_id

        form = CatalogForm(catalog_data, instance=catalog)
        if form.is_valid():
            #Save the form without commiting to the database
            catalog = form.save(commit=False)
            #Set the catalog relationship
            catalog.save()

            #Redirect back to the catalog detail page
            return redirect('Catalog-detail', catalog_id)
        
            
    context = {'form': form}
    return render(request, 'book_app/catalog_form.html', context)


#Restrict access to create a book if not logged in 
@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'] )
#Class to insert a book
def createBook(request, catalog_id):
    form = BookForm()
    catalog = Catalog.objects.get(pk= catalog_id)

    if request.method == 'POST':
        #Create a dictonairy with the form data
        book_data = request.POST.copy()
        book_data['catalog_id'] = catalog_id

        form = BookForm(book_data)
        if form.is_valid():
            #Save the form without commiting to the database
            book = form.save(commit=False)
            #Set the catalog relationship
            book.catalog = catalog
            book.save()

            #Redirect back to the catalog detail page
            return redirect('Catalog-detail', catalog_id)
        
            
    context = {'form': form}
    return render(request, 'book_app/catalog_form.html', context)

#Restrict access to update a book if not logged in
@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'] )
#Class to update a book
def updateBook(request, book_id, catalog_id):
    book = Book.objects.get(pk =book_id)
    catalog = Catalog.objects.get(pk=catalog_id)
    form = BookForm(instance = book)

    if request.method == 'POST':
        #Create a dictonairy with the form data
        book_data = request.POST.copy()
        book_data['catalog_id'] = catalog_id

        form = BookForm(book_data, instance=book)
        if form.is_valid():
            #Save the form without commiting to the database
            book = form.save(commit=False)
            #Set the catalog relationship
            book.catalog = catalog
            book.save()

            #Redirect back to the catalog detail page
            return redirect('Catalog-detail', catalog_id)
        
            
    context = {'form': form}
    return render(request, 'book_app/catalog_form.html', context)

#Restrict access to delete a book if not logged in
@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'] )
#Class to delete a book 
def deleteBook(request,book_id, catalog_id):

    #Get the book object
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        #Delete the book
        book.delete()

        #Redirect back to the catalog detail page
        return redirect('Catalog-detail', catalog_id)
        
            
    context = {'book': book}
    return render(request, 'book_app/book_delete.html', context)

# Had to create a custom view because it would not direct to the html file but rather the admin panel
def logoutUser(request):
    logout(request)
    return redirect('login')

#User will be directed to register 
def registerPage(request):
      form = CreateUserForm()

      if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                #Get the name from the form
                #name = form.cleaned_data.get('name')
                #Get the username from the form
                username = form.cleaned_data.get('username')
                #Get the group to add user 
                group = Group.objects.get(name = 'Book Members')
                user.groups.add(group)
                #Create a member to the database
                member = Member.objects.create(user=user, name = username)
                member.save()
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')


      context = {'form':form}
      return render(request, 'registration/register.html', context)

@login_required(login_url= 'login')
@allowed_users(allowed_roles= ['Book Members'] )
#User will be able to look at his own books and catalogs
def userPage(request):
    member = request.user.member
    form = MemberForm(instance = member)
    print('member', member)
    #Come back later to fix issue 
    #Wil not print member's catalogs
    catalogs = member.catalogs.all() if member.catalog else []
    #Debugging that allows me to see catalogs created 
    print('catalogs:', catalogs)
    for catalog in catalogs:
        print(f'Books in catalog {catalog.title}: {catalog.book_set.all()}')
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance = member)
        if form.is_valid():
            form.save()
    #context = {'catalogs':catalogs, 'form':form}
    context = {'member': member, 'form': form, 'catalogs': catalogs }
    return render(request, 'book_app/user.html', context)


       
