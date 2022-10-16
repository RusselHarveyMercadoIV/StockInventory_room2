from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import *
from registration.models import *


# Create your views here.


def index(request):
    request.session['username'] = None
    return render(request, 'registration/index.html')


class User_home(View):
    template = 'registration/user_home.html'

    def get(self, request):
        records_list = Sales.objects.order_by('dateOfSale')

        if request.session['username'] == None:
            return render(request, 'registration/index.html')
        try:
            cursor = connection.cursor()
            cursor.callproc('dbstockinventory.sales_transaction', [request.session['FDATE'],
                                                                   request.session['TDATE']])
            trans = list(cursor.fetchall())
            cursor.close()
        except:
            print("No Inputted Date yet...")
        return render(request, self.template, {'user_name': request.session['username'],
                                               'records': records_list,
                                               'trans': trans})

    def post(self, request):

        request.session['FDATE'] = request.POST['fromDate']
        request.session['TDATE'] = request.POST['toDate']

        return redirect(reverse('user_home'))


def user_logout(request):
    request.session['username'] = None
    return redirect(reverse('home'))


class RegisterCustomer(View):
    template = 'registration/register_customer.html'
    form = RegisterCustomerForm()

    def get(self, request):
        return render(request, self.template, {'form': self.form})

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
        return render(request, self.template, {'form': self.form})

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
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = user.username
                request.session['employee_id'] = user.user_ID
                return redirect(reverse('user_home'))
        except User.DoesNotExist:
            user = None
        return render(request, self.template, {'msg': 'Incorrect username/ password.'})


class EditProfile(View):
    template = 'registration/editProfile.html'

    def get(self, request):
        employee = Employee.objects.get(pk=request.session['employee_id'])
        form = RegisterEmployeeForm(instance=employee)
        return render(request, self.template, {'form': form})

    def post(self, request):
        employee = Employee.objects.get(pk=request.session['employee_id'])
        form = RegisterEmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            request.session['username'] = employee.username
        return redirect(reverse('user_home'))














