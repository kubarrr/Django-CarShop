from django import forms

from .models import Car

class NewCarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=('category', 'name', 'brand', 'transmission', 'price', 'description', 'image')

class EditCarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=('category','name', 'brand', 'transmission', 'price', 'description', 'image')