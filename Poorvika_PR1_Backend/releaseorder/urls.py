from django.urls import path,include
from.views import RoView,RoCreateView,RoListView,Ro_Edition_list,Ro_oub_date_list
# EditionView


urlpatterns = [
    path('ro',RoView.as_view(),name ='home'),
    path('ro/<pk>',RoCreateView.as_view(),name='create'),
    path('ro_list',RoListView.as_view(),name='ro_list'),
    path('ro_edition_list',Ro_Edition_list.as_view(),name='ro_list'),
    path('ro_Pub_date_list',Ro_oub_date_list.as_view(),name='ro_list'),

]
