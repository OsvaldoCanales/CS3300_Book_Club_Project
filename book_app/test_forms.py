from django.test import TestCase
from django.contrib.auth.models import User
from book_app.forms import CatalogForm 
from book_app.models import Catalog


# Create your tests here.

class CatalogFormTest(TestCase):
    
#Tests wheter the form saves the data correctly
    def test_form_save(self):
        #Input field forms
        valid_data = {'title': 'Sample Title', 'genre': 'Sample Genre', 'about': 'Sample About'}
        #Pass in the data 
        form = CatalogForm(data=valid_data)
        #Checks to see if its valid
        self.assertTrue(form.is_valid())

        catalog_instance = form.save(commit=False)
        #checks to see if the form saves an instance of the Catalog model
        self.assertIsInstance(catalog_instance, Catalog)

