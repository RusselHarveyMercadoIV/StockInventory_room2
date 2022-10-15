from . import views
from django.urls import path

app_name = 'addproduct'

urlpatterns = [
    path('', views.Product.as_view(), name = 'add_product'),
    path('editProduct', views.EditProduct.as_view(), name = 'edit_product'),
    path('deleteProduct', views.DeleteProduct.as_view(), name = 'delete_product'),
]