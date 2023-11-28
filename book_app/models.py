from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

#Set up Member list 
class Member(models.Model):
    name = models.CharField(max_length =200)
    email = models.CharField(max_length = 200)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    
#Define default string to return member name
    def __str__(self):
        return self.name
    
#If requested then return member details 
    def get_absolute_url(self):
        return reverse('member-detail', arg=[str(self.id)])

#Setup Book Catolog for different types of books
#Catalog can have as many books 
#Each catalog falls under only one user
class Catalog(models.Model):
    title = models.CharField(max_length=200)
    genre = models.TextField(null = True, blank = False)
    about = models.TextField(null=True, blank= False)
    member = models.ForeignKey(Member, on_delete= models.CASCADE, related_name='catalogs', null=True)                                
    # Default string to return genre title for Book Catalog
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Catalog-detail', args=[str(self.id)])
    
        
#Reader can list books into their catalog
#Book falls only under one catalog but there can be many books
class Book(models.Model):
    title =models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    description=models.TextField(null=True, blank=False)
    is_active = models.BooleanField(default=False)
    review = models.TextField(null=True, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, default= None)
   

# Return title of book 
    def __str__(self):
        return self.title

# Return url 
    def get_absolute_url(self):
        return reverse('Book-detail', args=[str(self.id)])
    




#class Book 