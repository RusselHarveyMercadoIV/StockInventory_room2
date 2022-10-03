from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from registration.forms import RegisterCustomerForm, RegisterEmployeeForm, Login, SupplierForm
from registration.models import *

# Create your views here.


def index(request):
    return render(request, 'registration/index.html')

def user_home(request):
    return render(request, 'registration/user_home.html')

class RegisterCustomer(View):
    template = 'registration/register_customer.html'
    form = RegisterCustomerForm()

    def get(self, request):
        return render(request, self.template, {'form':self.form})

    def post(self, request):
        self.form = RegisterCustomerForm(request.POST)
        if self.form.is_valid():
            self.form.save()
        else:
            print("unsucessful")
        return index(request)

class RegisterEmployee(View):
    template = 'registration/register_employee.html'
    form = RegisterEmployeeForm()

    def get(self, request):
        return render(request, self.template, {'form':self.form})

    def post(self, request):
        self.form = RegisterEmployeeForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('registration:login'))
        else:
            print("unsucessful")
        return index(request)


class Login(View):
    template = 'registration/login.html'
    form = Login()

    def get(self, request):
        return render(request, self.template, {'login':self.form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
            if user.password == password:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('registration:user_home'))
        except User.DoesNotExist:
            user = None

        return render(request, self.template,{'msg':'Incorrect username/ password.'})


class Supplier(View):
    template = 'supplier'
    form = SupplierForm()

    def get(self,request):
        return render(request,self.template,{'form': self.form})






