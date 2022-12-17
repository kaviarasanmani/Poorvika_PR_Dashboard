from rest_framework.response import Response
from rest_framework import generics
from .models import vendor
from .serializers import VendorSerializer
from user.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class VendorView(generics.ListCreateAPIView):
    queryset= vendor.objects.all()
    serializer_class = VendorSerializer
    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user,modified_by=self.request.user)
    # permission_classes =[IsAuthenticated]

class vendorCreateview(generics.RetrieveUpdateDestroyAPIView):
    queryset= vendor.objects.all()
    serializer_class = VendorSerializer

    # permission_classes = [IsAuthenticated,IsAdminUser]


    