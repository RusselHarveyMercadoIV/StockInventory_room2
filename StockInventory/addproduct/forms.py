from django.forms import ModelForm
from django import forms

from registration.models import Product


class ProductForm(ModelForm):
    prodName = forms.CharField(widget=forms.TextInput())
    prodQty = forms.IntegerField(widget=forms.NumberInput())
    prodPrice = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Product
        fields = '__all__'