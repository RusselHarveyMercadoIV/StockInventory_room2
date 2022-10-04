from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import Employee
from salesrecord.forms import SalesForm


# Create your views here.

class SalesRecord(View):
    template = 'salesrecord/sales_record.html'
    form = SalesForm()
    def get(self,request):
        employee = Employee.objects.get(pk = request.session['employee_id'])
        self.form = SalesForm(initial = {'eUser_ID': employee.user_ID})

        return render(request, self.template, {'form': self.form})
    def post(self, request):
        self.form = SalesForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('user_home'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))


