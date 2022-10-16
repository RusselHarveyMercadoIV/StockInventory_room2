from django.forms import ModelForm
from django import forms

from registration.models import Supplier
from registration.validators import checkNumber


class SupplierForm(ModelForm):
    # companyName = forms.CharField(widget=forms.TextInput())
    # address = forms.CharField(widget=forms.TextInput())
    mobileNumber = forms.CharField(validators=[checkNumber],
                                   max_length = 13)

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args,**kwargs)
        self.fields['companyName'].label = 'Company Name'
        self.fields['mobileNumber'].label = 'Mobile Number'

    class Meta:
        model = Supplier
        fields = '__all__'

