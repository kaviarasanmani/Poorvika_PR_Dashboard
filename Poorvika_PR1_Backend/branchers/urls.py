from django.urls import path
from .views import BranchCreateView,BranchView


urlpatterns = [
    path('branches',BranchView.as_view(),name ='home'),
    path('branches/<pk>',BranchCreateView.as_view(),name='create')

]
