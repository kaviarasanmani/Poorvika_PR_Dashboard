from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Publication(models.Model):
    pub_name = models.CharField(max_length=255)

    def __spoorvikatr__(self):
        return self.pub_name
    

class Edition(models.Model):
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    edition = models.CharField(max_length=255)

    def __str__(self):
        return 'Edition Name : {},Publication Name : {}'.format(self.edition, self.pub.pub_name)

class State(models.Model):
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state
    

class District(models.Model):
    district = models.CharField(max_length=255)
    state = models.ForeignKey(State,on_delete=models.CASCADE)


    def __str__(self):
        return 'District Name : {},State Name : {}'.format(self.district, self.state.state)

class Edition_save(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return 'Edition Name : {},district Name : {},Publication Name:{}'.format(self.edition, self.district.district,self.edition.pub.pub_name)





 