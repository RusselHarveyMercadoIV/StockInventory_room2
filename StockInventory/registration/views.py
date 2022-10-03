from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import *
from registration.models import *


# Create your views here.


def index(request):
    return render(request, 'registration/index.html')
def user_home(request):
    return render(request, 'registration/user_home.html', {'user_name':request.session['username']})

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
    registered = False

    def get(self, request):
        return render(request, self.template, {'form':self.form})

    def post(self, request):
        self.form = RegisterEmployeeForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            self.registered = True
        else:
            print("unsucessful")
        return render(request, self.template, {'form': self.form,
                                               'registered': self.registered})


class User_login(View):
    template = 'registration/login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
            if user.password == password:
                request.session['employee_id'] = user.user_ID
                request.session['username'] = user.username
                request.session['type'] = user.type
                return render(request,'registration/user_home.html', {'user_name': user.username})
        except User.DoesNotExist:
            user = None

        return render(request, self.template,{'msg':'Incorrect username/ password.'})



class Supplier(View):
    template = 'registration/supplier.html'
    form = SupplierForm()

    def get(self,request):
        return render(request,self.template,{'form': self.form})

    def post(self,request):
        self.form = SupplierForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return render(request,self.template,{'form':self.form})

class Product(View):
    template = 'product.html'
    form = ProductForm

    def get(self,request):
        return render(request,self.template,{'form': self.form})

    def post(self,request):
        self.form = ProductForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return render(request,self.template,{'form':self.form})


    








