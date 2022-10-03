from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.User_login.as_view(), name = 'login'),
    path('register_c/', views.RegisterCustomer.as_view(), name = 'register_customer'),
    path('register_e/', views.RegisterEmployee.as_view(), name = 'register_employee'),
    path('supplier/',views.Supplier.as_view(), name = 'supplier'),
    path('salesrecord/', views.SalesRecord.as_view(), name='sales_record'),
    path('product/',views.Product.as_view(), name = 'product'),

]