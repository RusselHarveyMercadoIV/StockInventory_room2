from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.models import Sales
from salesrecord.forms import SalesForm


# Create your views here.

class SalesRecord(View):
    template = 'salesrecord/sales_record.html'
    form = SalesForm()
    records_list = Sales.objects.order_by('salesID')
    def get(self,request):
        return render(request, self.template, {'form': self.form,
                                               'records' : self.records_list,
                                               'user_name':request.session['username']})
    def post(self, request):
        self.form = SalesForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return redirect(reverse('salesrecord:sales_record'))
        else:
            print("Unsuccesful")
        return redirect(reverse('user_home'))


