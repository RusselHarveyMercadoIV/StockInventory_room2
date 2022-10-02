from django.urls import path
from registration import views

app_name = 'registration'

urlpatterns = [
    path('', views.index, name="home"),
    path('register_c/', views.RegisterCustomer.as_view(), name = 'register_customer'),
    path('register_e/', views.RegisterEmployee.as_view(), name = 'register_employee')
]