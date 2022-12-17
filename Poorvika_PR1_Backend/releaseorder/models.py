from django.db import models

from branchers.models import branches
from vendors.models import vendor
from Edition.models import Edition
from user.models import User
# Create your models here.

class Release_order(models.Model):
    ro_date = models.DateField()
    Add_type = models.CharField(max_length=255)
    Size = models.CharField(max_length=255)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    gross_amount = models.DecimalField(max_digits=10,decimal_places=2)
    gst = models.IntegerField(default=1)
    gst_amount = models.DecimalField(max_digits=10,decimal_places=2)
    net_amunt = models.DecimalField(max_digits=10,decimal_places=2)
    billing_address = models.ForeignKey(branches, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # created_by = models.ForeignKey(User, related_name='release_order', on_delete=models.CASCADE)
    # modified_by = models.ForeignKey(User, related_name='modified_release_order', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ro_date},{self.Add_type}'
    



class Pub_date(models.Model):
    pub_date = models.DateField(null=True,blank=True)
    ro = models.ForeignKey(Release_order,related_name="pub_date", on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.pub_date},{self.ro}'



class R_edition(models.Model):
    edition = models.ForeignKey(Edition,related_name="edition_name", on_delete=models.CASCADE)
    ro = models.ForeignKey(Release_order,related_name="edition", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ro}'




# class testPublication(models.Model):
#     pub = models.CharField(max_length=255)
#     def __str__(self):
#         return f'{self.pub}'

# class testEdition(models.Model):
#     Edition = models.CharField(max_length=255)
#     pub = models.ForeignKey(testPublication,on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.Edition}'  


# class testDistrict(models.Model):
#     district = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     Edition =models.ForeignKey(testEdition,on_delete=models.CASCADE)



