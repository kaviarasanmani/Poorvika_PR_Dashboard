from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from user.models import User
# Create your models here.

class vendor(models.Model):

    Supplier_code= models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField()
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_reference = models.CharField(max_length=255, blank=True, null=True)
    # created_by = models.ForeignKey(User, related_name='vendor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # created_by = models.ForeignKey(User, related_name='vendor', on_delete=models.CASCADE)
    # modified_by = models.ForeignKey(User, related_name='modified_vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

