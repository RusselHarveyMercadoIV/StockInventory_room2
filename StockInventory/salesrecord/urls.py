from django.urls import path

from salesrecord import views

app_name = 'salesrecord'

urlpatterns = [
    path('addrecord/', views.SalesRecord.as_view(), name='sales_record'),
]