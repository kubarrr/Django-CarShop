from django import forms

from . models import Rent

class RentForm(forms.ModelForm):
    class Meta:
        model= Rent
        fields=('start', 'end', 'message')
        widgets = {
            'start': forms.TextInput(attrs={'type': 'date'}),
            'end': forms.TextInput(attrs={'type': 'date'}),
        }
