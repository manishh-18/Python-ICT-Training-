from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    cus_name = models.CharField(max_length=100)
    Product.pro_name
    Product.price
    Product.quantity
    Product.discount