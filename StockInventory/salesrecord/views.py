from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import Employee
from salesrecord.forms import SalesForm

from registration.models import Sales, Product


# Create your views here.

class SalesRecord(View):
    template = 'salesrecord/sales_record.html'
    form = SalesForm()

    def get(self,request):

        if request.session['username'] == None:
            return render(request, 'registration/index.html')

        employee = Employee.objects.get(pk = request.session['employee_id'])
        self.form = SalesForm(initial = {'eUser_ID': employee.user_ID})
        return render(request, self.template, {'form': self.form})

    def post(self, request):
        self.form = SalesForm(request.POST)

        if self.form.is_valid():
            form = self.form.save(commit = False)
            product = Product.objects.get(pk = request.POST['product_ID'])
            if form.quantity > product.prodQty:
                print("Value exceeds the current quantity!")
            else:
                form.save()
                product.prodQty -= form.quantity
                product.save()
            return redirect(reverse('user_home'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))


