from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from addproduct.forms import ProductForm

from registration.models import Product


# Create your views here.

edit_On = False

class Products(View):
    template = 'products/products.html'
    form = ProductForm

    def get(self,request):
        records_list = Product.objects.order_by('product_ID')
        if request.session['username'] == None:
            return render(request, 'registration/index.html')
        return render(request,self.template,{'form': self.form, 'records': records_list,
                                             'edit_On': edit_On})

    def post(self,request):
        self.form = ProductForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('user_home'))
        else:
            print("unsuccessful")


class EditProduct(View):
    template = 'products/products.html'

    def get(self,request, id):
        records_list = Product.objects.order_by('product_ID')
        product = Product.objects.get(pk=int(id))
        form = ProductForm(instance=product)
        return render(request, self.template, {'form': form, 'records':records_list,
                                               'edit_On': True})

    def post(self,request, id):
        prod = Product.objects.get(pk=int(id))
        form = ProductForm(request.POST,instance= prod)

        if form.is_valid():
            form.save()
        return redirect(reverse('addproduct:edit_product'))

class DeleteProduct(View):
    template = 'products/products.html'

    def get(self, request, id):
        records_list = Product.objects.order_by('product_ID')
        form = ProductForm()
        suppliers = Product.objects.get(pk=int(id))
        suppliers.delete()
        return render(request, self.template, {'form': form, 'records':records_list,
                                               'edit_On':edit_On})
