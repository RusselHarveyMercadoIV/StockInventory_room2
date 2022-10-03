from django.forms import ModelForm
from registration.models import Sales


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'