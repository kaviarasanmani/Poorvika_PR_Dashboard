from rest_framework import serializers

from .models import Purchase_order,Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields =(
            'title',
            'quantity',
            'unit_price',
            'net_amount',
            'gst',
            'gst_amount'

        )
        

class PurchaseorderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Purchase_order
        read_only_field =(
            'created_at',
            'modified_at',
            # 'created_by',
            # 'modified_by',

        )

        fields=(
                    'id',
                    'vendor',
                    'sender_reference',
                    # 'gross_amount',
                    'gst_amount',
                    'net_amount',
                    'items',
                    'branches',

        )
        # depth = 1


    def create(self, validated_data):
        item_data = validated_data.pop('items')
        purchase_order = Purchase_order.objects.create(**validated_data)
        for data in item_data:
            Item.objects.create(Purchase_order=purchase_order,**data)
        return purchase_order





    def update(self, instance, validated_data):
        items =validated_data.pop('items')

        item_list = list(instance.items.all())

        instance.sender_reference = validated_data.get('sender_reference',instance.sender_reference)
        instance.save()


        for data in items:
            items = item_list.pop(0)
            items.title = data.get('title',items.title)
            items.quantity = data.get('quantity',items.quantity)
            items.unit_price = data.get('unit_price',items.unit_price)
            items.net_amount = data.get('net_amount',items.net_amount)
            items.gst = data.get('gst',items.gst)
            items.gst_amount = data.get('gst_amount',items.gst_amount)
            items.save()
        return instance





class PurchaseorderSerializerList(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Purchase_order
        read_only_field =(
            'created_at',
            'modified_at',
            # 'created_by',
            # 'modified_by',

        )

        fields=(
                    'id',
                    'vendor',
                    'sender_reference',
                    # 'gross_amount',
                    'gst_amount',
                    'net_amount',
                    'items',
                    'branches',

        )
        depth = 2


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields =(
            'Purchase_order',
            'title',
            'quantity',
            'unit_price',
            'net_amount',
            'gst',
            'gst_amount'

        )
        depth = 1   