from django.urls import path
from .views import BOMCreateView,BOMView


urlpatterns = [
    path('bill_of_meterial',BOMView.as_view(),name ='home'),
    path('bill_of_meterial/<pk>',BOMCreateView.as_view(),name='create')

]
