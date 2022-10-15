from django.urls import path

from addsupplier import views

app_name = 'add_supplier'

urlpatterns = [
    path('supplier/',views.Suppliers.as_view(), name='supplier'),
    path('updateSupplier/<int:id>',views.UpdateSupplier.as_view(), name='update_supplier'),
    path('deleteSupplier/<int:id>',views.DeleteSupplier.as_view(), name='delete_supplier'),
]