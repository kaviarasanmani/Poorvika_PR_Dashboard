from user.models import User
from django.db import models

class branches(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    GST_number = models.CharField(max_length=266, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    # created_by = models.ForeignKey(User, related_name='branches', on_delete=models.CASCADE)
    # modified_by = models.ForeignKey(User, related_name='modified_branches', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'