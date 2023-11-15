from django.forms import ModelForm
from .models import Catalog,Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'genre', 'about')

class BookForm(ModelForm):
    class Meta: 
        model = Book
        fields = ('title', 'author', 'publication_date','description','is_active',
                  'review')
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']