from django.contrib import admin

# Register your models here.
from .models import Category, Car

admin.site.register(Category)
admin.site.register(Car)

