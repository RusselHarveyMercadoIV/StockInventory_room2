from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.

from registration.forms import SupplierForm
from registration.models import Supplier


# Create your views here.


class Supplier(View):
    template = 'supplier/supplier.html'
    form = SupplierForm()
    records_list = Supplier.objects.order_by('companyName')

    def get(self,request):
        return render(request, self.template, {'form': self.form,
                                               'records' : self.records_list,
                                               'user_name':request.session['username']})

    def post(self, request):
        self.form = SupplierForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('add_supplier:supplier'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))
