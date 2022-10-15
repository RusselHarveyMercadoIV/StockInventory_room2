from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from addsupplier.forms import SupplierForm
from registration.models import Supplier


# Create your views here.
edit_On = False

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


class UpdateSupplier(View):
    template = 'supplier/supplier.html'

    def get(self,request, id):
        records_list = Supplier.objects.order_by('supplier_ID')
        suppliers = Supplier.objects.get(pk=int(id))
        form = SupplierForm(instance=suppliers)
        edit_On = True
        return render(request, self.template, {'form': form, 'records':records_list})

    def post(self,request, id):
        supplier = Supplier.objects.get(pk=int(id))
        form = SupplierForm(request.POST,instance= supplier)

        if form.is_valid():
            form.save()
        return redirect(reverse('add_supplier:supplier'))


class DeleteSupplier(View):
    template = 'supplier/supplier.html'
    def get(self, request, id):
        records_list = Supplier.objects.order_by('supplier_ID')
        form = SupplierForm()
        suppliers = Supplier.objects.get(pk=int(id))
        suppliers.delete()
        return render(request, self.template, {'form': form, 'records':records_list})




