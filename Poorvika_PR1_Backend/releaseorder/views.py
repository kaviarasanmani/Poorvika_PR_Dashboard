# from rest_framework.response import Response
# from rest_framework import generics
# from .models import Release_order,Pub_date,R_edition
# from Edition.models import Edition
# from .serializers import Ro_serializer,realeaseSerializer,Ro_Edition_list,Ro_pub_date_list

# # RoListSerializer,\
    
# from user.models import User
# # ,Edition_Serializer

# class RoView(generics.ListCreateAPIView):
#     queryset = Release_order.objects.all()
#     serializer_class = realeaseSerializer

#     # def perform_create(self, serializer):
#     #     serializer.save(created_by=self.request.user,modified_by=self.request.user)

# class RoCreateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Release_order.objects.all()
#     serializer_class = realeaseSerializer




# # class RoListView(generics.ListAPIView):
# #     queryset = Release_order.objects.all()
# #     serializer_class = RoListSerializer


# class Ro_Edition_list(generics.ListAPIView):
#     queryset = R_edition.objects.all()
#     serializer_class = Ro_Edition_list

# class Ro_oub_date_list(generics.ListAPIView):
#     queryset = Pub_date.objects.all()
#     serializer_class = Ro_pub_date_list





# # class EditionView(generics.ListAPIView):
# #     queryset = Edition.objects.all()
# #     serializer_class = Edition_Serializer














# # from django.shortcuts import render

# # # Create your views here.
# # from rest_framework import generics
# # from .models import Pub_date,Edition,Release_order
# # from .serializers import edition_Serializer,realeaseSerializer
# # from rest_framework.views import APIView
# # from rest_framework.response import Response

# # class roviewlist(generics.ListAPIView):
# #     queryset = Release_order.objects.all()
# #     serializer_class = realeaseSerializer



# # class roviewset(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Release_order.objects.all()
# #     serializer_class = realeaseSerializer


from rest_framework.response import Response
from rest_framework import generics
from .models import Release_order,Pub_date,R_edition
from Edition.models import Edition
from .serializers import Ro_serializer,realeaseSerializer,RoListSerializer,\
    Ro_Edition_list,Ro_pub_date_list
from user.models import User
# ,Edition_Serializer

class RoView(generics.ListCreateAPIView):
    queryset = Release_order.objects.all()
    serializer_class = realeaseSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user,modified_by=self.request.user)

class RoCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Release_order.objects.all()
    serializer_class = realeaseSerializer




class RoListView(generics.ListAPIView):
    queryset = Release_order.objects.all()
    serializer_class = RoListSerializer


class Ro_Edition_list(generics.ListAPIView):
    queryset = R_edition.objects.all()
    serializer_class = Ro_Edition_list

class Ro_oub_date_list(generics.ListAPIView):
    queryset = Pub_date.objects.all()
    serializer_class = Ro_pub_date_list





# class EditionView(generics.ListAPIView):
#     queryset = Edition.objects.all()
#     serializer_class = Edition_Serializer














# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import Pub_date,Edition,Release_order
# from .serializers import edition_Serializer,realeaseSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class roviewlist(generics.ListAPIView):
#     queryset = Release_order.objects.all()
#     serializer_class = realeaseSerializer



# class roviewset(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Release_order.objects.all()
#     serializer_class = realeaseSerializer


    



