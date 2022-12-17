from rest_framework import serializers

from .models import vendor


class VendorSerializer(serializers.ModelSerializer):
    class  Meta:
        model = vendor

        read_only_field =(
            'created_at',
            'modified_at',
            # 'created_by',
            # 'modified_by',

        )
        fields =(
            'id',
            'Supplier_code',
            'name',
            'email',
            'phone',
            'address1',
            'address2',
            'zipcode',
            'city',
            'state',
            'country',
            'contact_person',
            'contact_reference',
            # '',
            # '',
            # '',
        )
