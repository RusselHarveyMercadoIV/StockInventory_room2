from django.forms import ModelForm
from django import forms
from .models import *


class RegisterCustomerForm(ModelForm):
    type = 'C'
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Customer
        exclude = ['type']

    def __init__(self, *args, **kwargs):
        super(RegisterCustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type


class RegisterEmployeeForm(ModelForm):
    type = 'E'
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Employee
        exclude = ['type']

    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type


class SupplierForm(ModelForm):
    companyName = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    contact = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Supplier
        fields = '__all__'


class ProductForm(ModelForm):
    prodName = forms.CharField(widget=forms.TextInput())
    prodQty = forms.IntegerField(widget=forms.NumberInput())
    prodPrice = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Product
        fields = '__all__'
