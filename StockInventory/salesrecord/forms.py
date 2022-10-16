from django.forms import ModelForm, NumberInput
from django import forms
from registration.models import Sales

from registration.models import Customer, Employee, Product


class SalesForm(ModelForm):
    cUser_ID = forms.ModelChoiceField(queryset = Customer.objects.only('user_ID'),label = "Customer")
    eUser_ID = forms.ModelChoiceField(queryset = Employee.objects.only('user_ID'),label = "Employee")
    product_ID = forms.ModelChoiceField(queryset = Product.objects.only('product_ID'),label = "Product")
    dateOfSale = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args,**kwargs)
        self.fields['dateOfSale'].label = 'Date'

    class Meta:
        model = Sales
        fields = '__all__'