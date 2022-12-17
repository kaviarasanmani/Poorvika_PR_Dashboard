from django.db import models


class ShowRoom(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self):
        return '{}{}'.format(self.id, self.location)


class Store(models.Model):
    D_CODE = models.CharField(max_length=5, null=True)
    SHOWROOM = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)
    SHORT_CODE = models.CharField(max_length=10, null=True)
    TYPE = models.CharField(blank=True, null=True, max_length=10)
    FLATE_HOUSE_NO = models.CharField(max_length=1000, null=True)
    STREET_BUILDING_NAME = models.CharField(max_length=500, null=True)
    LANDMARK = models.CharField(max_length=255, null=True)
    PINCODE = models.CharField(max_length=6, null=True)
    AREA = models.CharField(max_length=255, null=True)
    TALUK = models.CharField(max_length=255, null=True)
    DISTRICT = models.CharField(max_length=255, null=True)
    STATE = models.CharField(max_length=255, null=True)
    STATUS = models.CharField(max_length=255, null=True)
    DOB = models.DateField()
    CLOSED = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {} {} {}{}{}'.format(self.id, self.D_CODE, self.SHOWROOM, self.DISTRICT, self.STATUS,self.SHORT_CODE)


class Employee_master(models.Model):
    Emp_ID = models.CharField(max_length=10, null=True)
    Full_Name = models.CharField(max_length=255, null=True)
    Designation = models.CharField(max_length=560, null=True)
    Work_Area = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)
    Sub_Regions = models.CharField(max_length=100, null=True)
    Location_Type = models.CharField(max_length=255, null=True)
    Work_Area_Code = models.CharField(max_length=255, null=True)
    Office_City = models.CharField(max_length=255, null=True)
    Office_State = models.CharField(max_length=255, null=True)
    Region = models.CharField(max_length=225, null=True)
    Department_Code = models.CharField(max_length=255, null=True)
    Department = models.CharField(max_length=255, null=True)
    Gender = models.CharField(max_length=255, null=True)
    Date_of_Birth = models.DateField(null=True)
    Employee_Type = models.CharField(max_length=255)

    def __str__(self):
        return 'ID:{} Name:{} Designation:{}'.format(self.Emp_ID, self.Full_Name, self.Designation)


class Publication(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'ID :{}NAME :{}'.format(self.id, self.name)


class Edition(models.Model):
    Pub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    District = models.CharField(max_length=255)
    State = models.CharField(max_length=255, null=True, blank=True)
    Edition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return 'District :{} Publication :{}'.format(self.District, self.Pub)


class Page(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Layout(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EditionSave(models.Model):
    EditionDate = models.DateField(auto_now_add=True)
    EditionName = models.CharField(max_length=255,default=True,blank=True)
    EditionShowRoom = models.CharField(max_length=255,default=True,blank=True)
    EditionLocation = models.CharField(max_length=255,default=True,blank=True)
    EditionValue = models.CharField(max_length=255,default=True,blank=True)

    def __str__(self):
        return "Date :{} Edition :{} Edition Value :{} Edition Location :{}".format(self.EditionDate, self.EditionName, self.EditionValue, self.EditionLocation)
