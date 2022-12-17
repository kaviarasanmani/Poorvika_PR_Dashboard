from rest_framework.response import Response
from rest_framework import generics
from .models import branches
from .serializers import BranchesSerializer
from django.shortcuts import render,HttpResponse
from user.models import User




def home(request):
    return HttpResponse("Poorvika testing !!")

class BranchView(generics.ListCreateAPIView):
    queryset = branches.objects.all()
    serializer_class = BranchesSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user,modified_by=self.request.user)


class BranchCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = branches.objects.all()
    serializer_class = BranchesSerializer
