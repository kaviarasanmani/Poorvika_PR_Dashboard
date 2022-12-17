from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ShowRoom, Employee_master, Store, EditionSave
from .serializers import ShowRoomSerializer, StoreSerializer, PublicationSerializer, EditionSaveSerializer
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand, Layout, Publication, Edition
from rest_framework import serializers
from io import StringIO
from .utills import EditionData
from rest_framework import status



@csrf_exempt
def showroom(request):
    # if request.method == 'GET':
    #     show_room_data = ShowRoom.objects.all()
    #     serializer = ShowRoomSerializer(show_room_data, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    if request.method == 'GET':
        return JsonResponse("Welcome to django",safe=False)

class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['AREA', 'TALUK', 'DISTRICT', 'STATE']

class PublicationView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class RoSave(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        diff = int(self.request.query_params.get('diff'))
        bd = Brand.objects.filter(name=self.request.query_params.get('brand'))
        la = Layout.objects.filter(name=self.request.query_params.get('layout'))
        data_st = Store.objects.filter(STATE=self.request.query_params.get('state'))
        data_dis = Store.objects.filter(DISTRICT=self.request.query_params.get('district'))
        data_tal = Store.objects.filter(TALUK=self.request.query_params.get('taluk'))
        pub = Publication.objects.filter(name=self.request.query_params.get('publication'))
        # ed = Edition.objects.filter(name=self.request.query_params.get('edition'))
        print(diff)
        data_value = []
        # print("Edition",ed)
        print("Publication", pub)
        print("Layout", la)
        print("Brand", bd)
        print('district', data_dis)
        print("Tal", data_tal)
        if data_st.count() != 0:
            print("state :", data_st.count())
            data = data_st
            data_value.append(str(data))
            for r in data:
                print(r)
        elif data_dis.count() != 0:
            print("district :", data_dis.count())
            data = data_dis
            data_value.append(str(data))
            for r in data:
                print(r)
        elif data_tal.count() != 0:
            print("Tal :", data_tal.count())
            data = data_tal

            print("type", type(data_value))
            data_value.append(str(data))
            for r in data:
                print(r)

        return Response({"value": diff, "Count": data.count(), "single ": diff/data.count(), "name": data_value})


class EditionLocationView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        print("loc",self.request.data['Location'])
        print("val",self.request.data['Value'])
        print("edi",self.request.data['Edition'])

        el = EditionData()
        el.edition_loc(edition_location=self.request.data['Location'],
                       edition_value=int(self.request.data['Value']),
                       edition=self.request.data['Edition'],
                       )
        data = {
            "Edition": el.edition_display()["Edition"],
            "Search Location": el.edition_display()["Location"],
            "Get Location": el.edition_display()["Get Location"],
            "Value": self.request.data['Value'],
            "All Active Store": el.edition_display()['All Active Store'],
            "Total Average": el.edition_display()['Total Average'],
            "Store Count": el.edition_display()['Store Count'],
            "Store": el.edition_display()["Store"]
        }

        return Response(data)

    def post(self, request):

        el = EditionData()
        print(request.method)
        print(self.request.query_params.get('Location_all'))
        el.edition_loc(edition_location=self.request.data['Location'],
                       edition_value=int(self.request.data['Value']),
                       edition=self.request.data['Edition'])

        data = {
            "Edition": el.edition_display()["Edition"],
            "Search Location": el.edition_display()["Location"],
            "Get Location": el.edition_display()["Get Location"],
            "Value": self.request.data['Value'],
            "All Active Store": el.edition_display()['All Active Store'],
            "Total Average": el.edition_display()['Total Average'],
            "Store Count": el.edition_display()['Store Count'],
            "SHOWROOM": el.edition_display()["SHOWROOM"]
        }

        return Response(data)


class EditionLocationAllView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data_value = self.request.data['Value']
        data_store = Store.objects.filter(STATE=self.request.data['state']).count()
        data_store_active = Store.objects.filter(STATE=self.request.data['state'], STATUS='ACTIVE').count()
        # data_district = Store.objects.filter(DISTRICT=self.request.query_params.get('district'))
        # data_taluk = Store.objects.filter(TALUK=self.request.query_params.get('taluk'))

        data = {
            "Edition": self.request.data['Edition'],
            "State": self.request.data['state'],
            "Value": int(self.request.data['Value']),
            "Average": round(data_value / data_store_active),
            "All Store": data_store,
            "Active Store": data_store_active
        }
        for store_id in Store.objects.filter(STATE=self.request.data['state'], STATUS='ACTIVE'):
            data["SHOWROOM NAME :" + str(store_id.SHOWROOM)] = store_id.SHOWROOM
        print(data)
        return Response(data)

    def post(self, request, *args, **kwargs):
        data_value = int(self.request.data['Value'])
        data_store = Store.objects.filter(STATE=self.request.data['state']).count()
        data_store_active = Store.objects.filter(STATE=self.request.data['state'], STATUS='ACTIVE').count()

        data = {
            "Edition": self.request.data['Edition'],
            "State": self.request.data['state'],
            "Value": int(self.request.data['Value']),
            "Average": round(data_value/data_store_active),
            "All Store" :data_store,
            "Active Store":data_store_active
        }

        for store_id in Store.objects.filter(STATE=self.request.data['state'], STATUS='ACTIVE'):
            # data["Store Id " + str(store_id.SHORT_CODE)] = store_id.SHORT_CODE
            data["SHOWROOM NAME :" + str(store_id.SHOWROOM.location)] = store_id.SHOWROOM.location
            # ed.EditionLocation = store_id.SHORT_CODE
            # ed.EditionName = self.request.data['Edition']
            # ed.EditionValue = round(data_value/data_store)
            # ed.save()
        return Response(data)


class EditionLocationList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            "Edition": self.request.data['Edition'],
            "Value": self.request.data['Value'],
            "Edition_location": self.request.data['Edition_location'],
            "Average": round(self.request.data['Value'] / len(self.request.data['Edition_location']))
        }
        for r in data["Edition_location"]:
            for st in Store.objects.filter(D_CODE=r):
                data[st.SHORT_CODE] = st.STATE
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = {
            "Edition": self.request.data['Edition'],
            "Value": self.request.data['Value'],
            "Edition_location": self.request.data['Edition_location'],
            "Average": round(self.request.data['Value']/len(self.request.data['Edition_location']))
        }

        for r in data["Edition_location"]:
            ed = EditionSave()
            for st in Store.objects.filter(D_CODE=r):
                ed.EditionLocation = st.SHORT_CODE
                ed.EditionValue = data['Average']
                ed.EditionName = data['Edition']
                ed.save()

        return Response(data)
