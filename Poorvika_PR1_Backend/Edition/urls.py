from django.urls import path
from .views import *
from .views import my_view,UserCountView


urlpatterns = [
    
    path('Edition',Edition_list_view.as_view(),name='Edition'),
    path('Publication',Publication_list_view.as_view(),name='Publications'),
    path('Edition_Add',EditionSaveView.as_view(),name='Edition_Add'),
    path('State',StateView.as_view(),name='StateView'),
    path('District',DistrictView.as_view(),name='DistrictView'),
    path('Edition_save_list',EditionSavelistView.as_view(),name='Edition_save_list'),
    path('po_ro_count',UserCountView.as_view(),name='count'),
    path('Count',my_view,name='my_view'),

]
    
