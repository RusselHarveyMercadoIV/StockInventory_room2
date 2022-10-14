from django.urls import path

from addsupplier import views

app_name = 'add_supplier'

urlpatterns = [
    path('supplier/',views.Suppliers.as_view(), name='supplier'),
]