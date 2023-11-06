from django.forms import ModelForm
from .models import Catalog,Book

class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'genre', 'about')

class BookForm(ModelForm):
    class Meta: 
        model = Book
        fields = ('title', 'author', 'publication_date','description','is_active',
                  'review')