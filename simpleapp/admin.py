from django.contrib import admin
from django.contrib import admin
from .models import Category, Product, News


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(News)

# Register your models here.
