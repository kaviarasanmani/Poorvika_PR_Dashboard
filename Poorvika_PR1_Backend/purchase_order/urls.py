from django.urls import path
from .views import PoCreateView,PoView,PoListView,ItemView

from .views import *
urlpatterns = [
    path('po',PoView.as_view(),name = 'home'),
    path('po/<pk>',PoCreateView().as_view(),name='create'),
    path('po_list',PoListView().as_view(),name='list'),
    path('items_list',ItemView().as_view(),name='items_list')
    
]
