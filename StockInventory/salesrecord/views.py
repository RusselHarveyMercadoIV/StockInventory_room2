from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import Employee, Sales, Product, Transactions, Supplier
from salesrecord.forms import SalesForm



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
                rev = form.quantity * product.prodPrice
                try:
                    trans_record = Transactions.objects.get(product= product.product_ID)
                    update_record = Transactions(transactionID=trans_record.transactionID,
                                                 salesCount=(trans_record.salesCount + rev),
                                                 supplier=trans_record.supplier,
                                                 product=trans_record.product)
                    update_record.save()

                except:
                    supp = Supplier.objects.get(supplier_ID=product.supplier_ID.supplier_ID)
                    Transactions.objects.create(salesCount=rev,
                                                supplier=supp,
                                                product=product)
                form.save()
                product.prodQty -= form.quantity
                product.save()
            return redirect(reverse('user_home'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))


