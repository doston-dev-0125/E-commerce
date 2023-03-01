from django.contrib import admin
from .models import Category,Sub_Category,Product,Order,Brand

admin.site.register([Category,Sub_Category,Product,Order,Brand])
