from django.urls import path

from salesrecord import views

app_name = 'salesrecord'

urlpatterns = [
    path('salesrecord/', views.SalesRecord.as_view(), name='sales_record'),
]