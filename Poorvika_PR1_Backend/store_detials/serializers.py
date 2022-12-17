from rest_framework import serializers
from .models import ShowRoom, Store, Publication, Edition


class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = ['id', 'location']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'AREA', 'TALUK', 'DISTRICT', 'STATE']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'name']


class EditionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ['id','EditionName','EditionShowRoom','EditionLocation','EditionValue']



