from statistics import mode
from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id = models.AutoField
    hotel_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
