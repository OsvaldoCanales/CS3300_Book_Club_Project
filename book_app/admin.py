from django.contrib import admin
from .models import Catalog,Book

# Register your models here.
admin.site.register(Catalog)
admin.site.register(Book)
