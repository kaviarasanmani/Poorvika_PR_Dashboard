from rest_framework import serializers
from .models import bill_of_material


class bill_of_materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = bill_of_material
        
        fields ='__all__'
        # depth = 1
