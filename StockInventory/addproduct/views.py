from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from addproduct.forms import ProductForm


# Create your views here.

class Product(View):
    template = 'products/products.html'
    form = ProductForm

    def get(self,request):
        if request.session['username'] == None:
            return render(request, 'registration/index.html')
        return render(request,self.template,{'form': self.form})

    def post(self,request):
        self.form = ProductForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('user_home'))
        else:
            print("unsuccessful")


class EditProduct(View):
    template = 'supplier/supplier.html'

    def get(self,request, id):
        records_list = Product.objects.order_by('product_ID')
        product = Product.objects.get(pk=int(id))
        form = ProductForm(instance=product)
        return render(request, self.template, {'form': form, 'records':records_list})

    def post(self,request, id):
        supplier = Product.objects.get(pk=int(id))
        form = ProductForm(request.POST,instance= supplier)

        if form.is_valid():
            form.save()
        return redirect(reverse('add_supplier:supplier'))

class DeleteProduct(View):
    template = 'supplier/supplier.html'

    def get(self, request, id):
        records_list = Product.objects.order_by('product_ID')
        form = ProductForm()
        suppliers = Product.objects.get(pk=int(id))
        suppliers.delete()
        return render(request, self.template, {'form': form, 'records':records_list})
