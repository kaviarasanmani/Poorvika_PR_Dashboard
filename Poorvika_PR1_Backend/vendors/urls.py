from django.urls import path 
from .views import vendorCreateview,VendorView


urlpatterns = [
    path('vendor',VendorView.as_view(),name='home'),
    path('vendor/<pk>',vendorCreateview().as_view(),name='home')
]
