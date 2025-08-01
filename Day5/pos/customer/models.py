from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    
    