from rest_framework import serializers
from .models import Edition,Publication,Edition_save,State,District

class Edition_Serialiezer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = "__all__"                                           
        depth = 1





class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"
        # depth = 1


class EditionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition_save
        fields = "__all__"
        # depth = 1


class EditionSavelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition_save
        fields = "__all__"
        depth = 2


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields ="__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields ="__all__"
