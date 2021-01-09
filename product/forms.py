from django import forms
from .models import ShippingAdress


class ShippingAddress(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['address', 'city', 'state', 'zipcode', 'email']
        labels = {
            'address':'',
            'city':'',
            'state':'',
            'zipcode':'',
            'email':'',
        }
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Address:'}),
            'city': forms.TextInput(attrs={'placeholder': 'City:'}),
            'state': forms.TextInput(attrs={'placeholder': 'State:'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode:'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email:'}),
        }
