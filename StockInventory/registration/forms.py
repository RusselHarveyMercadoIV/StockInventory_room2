from django.forms import ModelForm
from registration.models import User, Customer, Employee

class RegisterCustomerForm(ModelForm):
    type = 'C'
    class Meta:
        model = Customer
        exclude = ['type']

    def __init__(self, *args, **kwargs):
        super(RegisterCustomerForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type

class RegisterEmployeeForm(ModelForm):
    type = 'E'
    class Meta:
        model = Employee
        exclude = ['type']

    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type