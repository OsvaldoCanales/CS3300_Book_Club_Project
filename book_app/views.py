from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from .models import Catalog, Book



# HomePage 
def index(request):
    active_books = Book.objects.filter(is_active=True)
    print("Active Books available", active_books )
    return render(request, 'book_app/index.html', {'Book Catalogs':active_books})


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
        context["books"] = Book.objects.filter(book=self.object)
        return context

#List all available books
class BookListView(generic.ListView):
    model = Book

#List the detail of that book 
class BookDetailView(generic.DetailView):
    model = Book

