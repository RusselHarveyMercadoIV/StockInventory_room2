from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.forms import SupplierForm

# Create your views here.


class Supplier(View):
    template = 'supplier/supplier.html'
    form = SupplierForm()

    def get(self,request):
        return render(request, self.template, {'form': self.form,
                                               'user_name':request.session['username']})

    def post(self, request):
        self.form = SupplierForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('add_supplier:supplier'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))
