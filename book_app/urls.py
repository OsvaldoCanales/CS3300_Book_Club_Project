from django.urls import path
from .import views

urlpatterns = [
# path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in view.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %})>Hoe</a>.

path('', views.index, name= 'index'),
path('catalogs/', views.CatalogListView.as_view(), name = 'catalogs'),
path('catalog/<int:pk>/', views.CatalogDetailView.as_view(), name ='Catalog-detail'),
path('books/', views.BookDetailView(), name = 'books'),
path('Book/<int:pk>/', views.BookDetailView.as_view(), name ='Book-detail'),
]