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