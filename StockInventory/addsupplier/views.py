from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.forms import SupplierForm

# Create your views here.


class Supplier(View):
    template = 'supplier/supplier.html'
    form = SupplierForm()

    def get(self,request):
        if request.session['username'] == None:
            return render(request, 'registration/index.html')
        return render(request, self.template, {'form': self.form})

    def post(self, request):
        self.form = SupplierForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('user_home'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))
