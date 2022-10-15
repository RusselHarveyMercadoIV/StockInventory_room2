from django.forms import ModelForm, NumberInput
from django import forms
from registration.models import Sales


class SalesForm(ModelForm):
    dateOfSale = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Sales
        fields = '__all__'