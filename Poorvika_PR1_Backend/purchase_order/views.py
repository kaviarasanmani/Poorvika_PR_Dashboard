from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators import csrf

from .models import Item,Purchase_order
from .serializers import PurchaseorderSerializer,ItemSerializer,PurchaseorderSerializerList,ItemListSerializer

from user.models import User

class PoView(generics.ListCreateAPIView):
    queryset = Purchase_order.objects.all()
    serializer_class = PurchaseorderSerializer

    




class PoListView(generics.ListAPIView):
    queryset = Purchase_order.objects.all()
    serializer_class = PurchaseorderSerializerList



class PoCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase_order.objects.all()
    serializer_class = PurchaseorderSerializer


class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer



    # def get_permissions(self):
    #     if self.request.method in ['GET','PUT','DELETE']:
    #         return [permissions.IsAdminUser()]
    #     return[permissions.IsAuthenticated()]
