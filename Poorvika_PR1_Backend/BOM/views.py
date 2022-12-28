from django.shortcuts import render
from .models import bill_of_material
from .serializers import bill_of_materialSerializer
from rest_framework.response import Response
from rest_framework import generics

class BOMView(generics.ListCreateAPIView):
    queryset = bill_of_material.objects.all()
    serializer_class = bill_of_materialSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user,modified_by=self.request.user)


class BOMCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = bill_of_material.objects.all()
    serializer_class = bill_of_materialSerializer
