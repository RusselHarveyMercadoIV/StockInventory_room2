from . import views
from django.urls import path

app_name = 'addproduct'

urlpatterns = [
    path('', views.Product.as_view(), name = 'add_product'),
]