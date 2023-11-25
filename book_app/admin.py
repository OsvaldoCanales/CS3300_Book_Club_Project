from django.contrib import admin
from .models import Catalog,Book, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Catalog)
admin.site.register(Book)
