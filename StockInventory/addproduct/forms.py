from django.forms import ModelForm
from django import forms

from registration.models import Product


class ProductForm(ModelForm):
    prodName = forms.CharField(widget=forms.TextInput())
    prodQty = forms.IntegerField(widget=forms.NumberInput())
    prodPrice = forms.IntegerField(widget=forms.NumberInput())

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args,**kwargs)
        self.fields['prodName'].label = 'Product Name'
        self.fields['prodQty'].label = 'Product Quantity'
        self.fields['prodPrice'].label = 'Product Price'

    class Meta:
        model = Product
        fields = '__all__'