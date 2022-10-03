from django.forms import ModelForm

from registration.models import Supplier


class SupplierForm(ModelForm):
    # companyName = forms.CharField(widget=forms.TextInput())
    # address = forms.CharField(widget=forms.TextInput())
    # contact = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Supplier
        fields = '__all__'