from django.db import models
# Create your models here.
import decimal
from datetime import timedelta
from branchers.models import branches
from vendors.models import vendor
from user.models import User


class Purchase_order(models.Model):
    vendor = models.ForeignKey(vendor, related_name='invoices', on_delete=models.CASCADE)
    sender_reference = models.CharField(max_length=255, blank=True, null=True)   
    # gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=12, decimal_places=2)
    net_amount = models.DecimalField(max_digits=12, decimal_places=2)
    # team = models.ForeignKey(Team, related_name='invoices', on_delete=models.CASCADE)
    # created_by = models.ForeignKey(User, related_name='created_Purchase_order', on_delete=models.CASCADE)
    # modified_by = models.ForeignKey(User, related_name='modified_Purchase_order', on_delete=models.CASCADE)
    branches = models.ForeignKey(branches,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Item(models.Model):
    Purchase_order = models.ForeignKey(Purchase_order, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12,decimal_places=2)
    net_amount = models.DecimalField(max_digits=12,decimal_places=2)
    gst = models.IntegerField(default=0)
    # discount = models.IntegerField(default=0)
    gst_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def get_gross_amount(self):
        vat_rate = decimal.Decimal(self.vat_rate/100)
        return self.net_amount + (self.net_amount * vat_rate)