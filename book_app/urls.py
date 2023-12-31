from django.urls import path, include
from .import views



urlpatterns = [
# path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in view.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %})></a>.

path('', views.index, name= 'index'),
path('catalogs/', views.CatalogListView.as_view(), name = 'catalogs'),
path('catalog/<int:pk>/', views.CatalogDetailView.as_view(), name ='Catalog-detail'),
path('catalog/<int:catalog_id>/update_catalog/', views.updateCatalog, name ='update_catalog'),
path('books/', views.BookDetailView.as_view(), name = 'books'),
path('book/<int:pk>/', views.BookDetailView.as_view(), name ='Book-detail'),
path('catalog/<int:catalog_id>/create_book/', views.createBook, name = 'create_book' ),
path('catalog/<int:book_id>/delete_book/<int:catalog_id>/',views.deleteBook, name = 'delete_book'),
path('catalog/<int:book_id>/update_book/<int:catalog_id>/', views.updateBook, name = 'update_book'), 
#Add Django site authentication urls (for login, logout, password maangement)
path('accounts/logout/', views.logoutUser, name = 'logout' ),
path('user/', views.userPage, name = 'user_page' ),
path('user/createCatalog/', views.createCatalog, name = 'create_catalog'),
path('user/catalogs/', views.catalogsView, name='catalogs_view'),
path('accounts/register/', views.registerPage, name = 'register_page'),
path('accounts/', include('django.contrib.auth.urls')),

]