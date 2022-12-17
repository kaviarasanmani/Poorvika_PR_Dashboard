from django.contrib import admin

# Register your models here.
from .models import Purchase_order,Item
admin.site.register(Purchase_order)
admin.site.register(Item)


