from django.forms import ModelForm
from django import forms

from registration.models import Supplier
from registration.forms import checkNumber


class SupplierForm(ModelForm):
    # companyName = forms.CharField(widget=forms.TextInput())
    # address = forms.CharField(widget=forms.TextInput())
    mobileNumber = forms.CharField(validators=[checkNumber])

    class Meta:
        model = Supplier
        fields = '__all__'