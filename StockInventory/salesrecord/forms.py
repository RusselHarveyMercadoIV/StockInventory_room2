from django.forms import ModelForm, forms, NumberInput
from registration.models import Sales


class SalesForm(ModelForm):
    dateOfSale = forms.FileField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Sales
        fields = '__all__'