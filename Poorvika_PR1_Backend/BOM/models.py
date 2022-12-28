from django.db import models

class bill_of_material(models.Model):
    material_code = models.CharField(max_length=255)
    material_type = models.CharField(max_length=255)
    material = models.TextField(max_length=255)
    material_price = models.IntegerField()
    
