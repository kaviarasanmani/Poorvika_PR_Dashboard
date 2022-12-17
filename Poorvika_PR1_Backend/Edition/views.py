from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import Edition_Serialiezer,PublicationSerializer,EditionSaveSerializer,StateSerializer,DistrictSerializer,EditionSavelistSerializer
from releaseorder.models import *

class Edition_list_view(generics.ListAPIView):
    queryset = Edition.objects.all()
    serializer_class = Edition_Serialiezer


class Publication_list_view(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    
class EditionSaveView(generics.ListCreateAPIView):
    queryset = Edition_save.objects.all()
    serializer_class = EditionSaveSerializer

class EditionSavelistView(generics.ListAPIView):
    queryset = Edition_save.objects.all()
    serializer_class = EditionSavelistSerializer
    
class StateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    
class DistrictView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    
# class count()

from django.http import HttpResponse

def my_view(request):
    # if request.method == 'GET':
        # <view logic>
    count = Release_order.objects.count()
    count_edition = R_edition.objects.count()

    content={
        count:'test',
        count_edition:'cygdwcf'

    }
    return HttpResponse(content=content)


from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from purchase_order.models import *

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        ro_count = Release_order.objects.count()
        po_count = Purchase_order.objects.count()

        # po_value= Purchase_order.objects.annotate(sum(net_amount))

        content = {'ro_count': ro_count,
                    'po_count':po_count,
                    # 'po_count':po_count

                    }
        return Response(content)