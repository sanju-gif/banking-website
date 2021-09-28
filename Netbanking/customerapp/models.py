from django.db import models
from django.db.models import Model
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    account = models.IntegerField(default=0)
    balance = models.FloatField(default=0)
    address = models.CharField(max_length=100) 
    pub_date =models.DateTimeField('date published',default=timezone.now()) #,self.pub_date

    def __str__(self):
        return "{0},{1},{2},{3},{4}".format(self.name,self.account,self.balance,self.address,self.pub_date)
    

