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


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class Supplier(forms.Form):
    product_ID = forms.AutoField(widget = forms.NumberInput())
    prodName = forms.CharField(widget = forms.TextInput())
    prodQty = forms.IntegerField(widget= forms.NumberInput)
    prodPrice = forms.IntegerField(widget = forms.IntegerField())
    supplier_ID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    class Meta: Supplier
    fields = '__all__'

