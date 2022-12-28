
from django.contrib import admin
from django.urls import path, include
# from rest_auth.views

from rest_framework import routers
from branchers import views
from branchers.views import home



urlpatterns = [
    path('backend/', admin.site.urls),
    path('',views.home,name='home'),
    path('api/v1/', include('releaseorder.urls')),
    path('api/v1/', include('branchers.urls')),
    path('api/v1/',include('vendors.urls')),
    path('api/v1/', include('purchase_order.urls')),
    path('api/v1/',include('store_detials.urls')),
    path('api/v1/',include('user.urls')),
    path('api/v1/',include('Edition.urls')),
    path('api/v1/',include('BOM.urls')),
]


