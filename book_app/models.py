from django.db import models
from django.urls import reverse

# Create your models here.


#Setup Book Catolog for different types of books
class Catalog(models.Model):
    title = models.CharField(max_length=200)
    genre = models.TextField(null = True, blank = False)
    about = models.TextField(null=True, blank= False)
    
    # Default string to return genre title for Book Catalog
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Catalog-detail', args=[str(self.id)])
    
        
#Reader can list books into their catolog
class Book(models.Model):
    title =models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=False)
    is_active = models.BooleanField(default=False)
    review = models.TextField(null=True, blank=True)
   

# Return title of book 
    def __str__(self):
        return self.title

# Return url 
    def get_absolute_url(self):
        return reverse('Book-detail', args=[str(self.id)])



