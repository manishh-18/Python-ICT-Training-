from django.db import models

# Create your models here.
class Product(models.Model):
    pro_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    discount = models.IntegerField()