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


def checkNumber(value):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
    if (value[0] == '+') and (len(value) == 13):
        for digit in value[1:]:
            if digit not in numbers:
                raise forms.ValidationError("This is not a Number!")
    else:
        raise forms.ValidationError("Invalid Number!")

class RegisterEmployeeForm(ModelForm):
    type = 'E'
    password = forms.CharField(widget=forms.PasswordInput())
    mobileNumber = forms.CharField(validators=[checkNumber], max_length = 13)
    class Meta:
        model = Employee
        exclude = ['type', 'mobileNumber']

    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type

