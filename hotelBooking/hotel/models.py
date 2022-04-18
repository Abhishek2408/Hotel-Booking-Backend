from distutils.command.upload import upload
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id = models.AutoField
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,default="")
    location_url = models.URLField(max_length=500,default="")
    category = models.CharField(max_length=100,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    main_image = models.ImageField(upload_to="hotel/images",default="")

    def __str__(self):
        return self.hotel_name

class Contact(models.Model):
    desc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")
    desc = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name
