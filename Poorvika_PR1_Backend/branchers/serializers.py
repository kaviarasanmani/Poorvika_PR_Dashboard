from rest_framework import serializers
from .models import branches


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = branches
        read_only_field =(
            'created_at',
            'modified_at',
            # 'created_by',
            # 'modified_by',

        )
        fields =(
            'id',
            'name',
            'phone',
            'GST_number',
            'email',
            'address1',
            'address2',
            'pincode',
            'city',
            'state',
            'country',

            # '',
            # '',
            # '',

        )
        depth = 1
