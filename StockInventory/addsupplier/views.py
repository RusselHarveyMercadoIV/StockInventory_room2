from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from addsupplier.forms import SupplierForm
from registration.models import Supplier


# Create your views here.


class Suppliers(View):
    template = 'supplier/supplier.html'
    form = SupplierForm()

    def get(self,request):
        records_list = Supplier.objects.order_by('supplier_ID')
        if request.session['username'] == None:
            return render(request, 'registration/index.html')
        return render(request, self.template, {'form': self.form, 'records':records_list})

    def post(self, request):
        records_list = Supplier.objects.order_by('supplier_ID')
        self.form = SupplierForm(request.POST)
        if self.form.is_valid():
            self.form.save()
        else:
            print("Unsuccesful")
        return render(request, self.template, {'form': self.form, 'records':records_list})


