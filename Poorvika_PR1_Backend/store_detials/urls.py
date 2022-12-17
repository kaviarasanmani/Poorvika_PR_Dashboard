from .views import *
from django.urls import path

urlpatterns = [
    path('store_all', showroom, name='home'),
    path('StoreList/', StoreList.as_view(),name='store'),
    path('test/', RoSave.as_view(), name='test'),
    path('Edition_loc/', EditionLocationView.as_view(), name='Edition_loc'),
    path('Edition_by_state/', EditionLocationAllView.as_view(), name='Edition_by_state'),
    path('Edition_by_store/', EditionLocationList.as_view(), name='Edition_by_store'),
    path('pub/', PublicationView.as_view(), name='pub'),

    # path("edsearch/",EditionSearch.as_view(),name='edsearch')

]
