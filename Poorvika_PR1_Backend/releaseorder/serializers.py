from rest_framework import serializers


from.models import R_edition,Release_order,Pub_date,R_edition
from Edition.models import Edition
# class Edition_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Edition
#         fields = "__all__"                                           
#         depth = 1

class Ro_serializer(serializers.ModelSerializer):
    class Meta:
        model = R_edition
        fields =(
            'edition',
        )   
        # depth=2
# class edition_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Edition
#         fields =(
#             # 'id',   
#             'edition',
#         )
#         depth = 1



class Pub_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pub_date
        fields = (
            'pub_date',
        )
        depth = 1

class realeaseSerializer(serializers.ModelSerializer):
    edition = Ro_serializer(many=True)
    pub_date = Pub_Serializer(many=True)
    class Meta:
        model = Release_order
        read_only_field =(
            'created_at',
            'modified_at',
            # 'created_by',
            # 'modified_by',

        )
        fields =(
            'id',
            'ro_date',
            'Add_type',
            'Size',
            'vendor',
            'color',
            'gross_amount',
            'gst',
            'gst_amount',
            'net_amunt',
            'billing_address',   
            'edition',
            'pub_date',
        )
        # depth = 1

    def create(self, validated_data):
        edition_date = validated_data.pop('edition')
        pub_date = validated_data.pop('pub_date')

        ro=Release_order.objects.create(**validated_data)
        for data in edition_date: 
            R_edition.objects.create(ro=ro,**data)
        for data in pub_date:
            Pub_date.objects.create(ro=ro,**data)
        return ro

    def update(self, instance, validated_data):
        edition = validated_data.pop('edition')
        pub_date = validated_data.pop('pub_date')

        edition_list = list(instance.edition.all())
        pub_list = list(instance.pub_date.all())

        instance.ro_date = validated_data.get('ro_date',instance.ro_date)
        instance.save()


        for data in edition:
            edition = edition_list.pop(0)
            edition.edition = data.get('edition',edition.edition)
            edition.save()

        for data in pub_date:
            pub = pub_list.pop(0)
            pub.pub_date = data.get('pub_date',pub.pub_date)
            pub.save()

        return instance



class RoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release_order
        fields = "__all__"
        depth = 1


class Ro_Edition_list(serializers.ModelSerializer):
    class Meta:
        model = R_edition
        fields = "__all__"
        depth = 1


class Ro_pub_date_list(serializers.ModelSerializer):
    class Meta:
        model = Pub_date
        fields = "__all__"
        depth = 1


