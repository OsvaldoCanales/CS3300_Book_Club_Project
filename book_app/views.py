from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from .models import Catalog, Book
from .forms import CatalogForm, BookForm



# HomePage 
def index(request):
    active_books = Book.objects.filter(is_active=True)
    print("Active Books available", active_books )
    return render(request, 'book_app/index.html', {'active_books':active_books})


#List all available Catalogs
# Note: Since we have a generic List implemented, 
# it will automatically render a catalog_list.html that we need to create
class CatalogListView(generic.ListView):
    model = Catalog

#List detail of catalog
class CatalogDetailView(generic.DetailView):
    model = Catalog

    #Get all books associated with that catalog 
    def get_context_data(self, **kwargs):
        #Call the base implmenatation first to get a context
        context = super().get_context_data(**kwargs)
        #Add in a QuerySet of all the projects
        context["books"] = Book.objects.filter(catalog=self.object)
        return context

#List all available books
class BookListView(generic.ListView):
    model = Book

#List the detail of that book 
class BookDetailView(generic.DetailView):
    model = Book

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


#Class to delete a book 
def deleteBook(request,book_id, catalog_id):

    #Get the book object
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        #Delete the book
        book.delete()

        #Redirect back to the catalog detail page
        return redirect('Catalog-detail', catalog_id)
        
            
    context = {'form': book}
    return render(request, 'book_app/book_delete.html', context)
