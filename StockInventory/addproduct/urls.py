from . import views
from django.urls import path

app_name = 'addproduct'

urlpatterns = [
    path('', views.Products.as_view(), name = 'add_product'),
    path('editProduct/<int:id>', views.EditProduct.as_view(), name = 'edit_product'),
    path('deleteProduct/<int:id>', views.DeleteProduct.as_view(), name = 'delete_product'),
]