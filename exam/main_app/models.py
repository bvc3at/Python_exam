from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CAT = (('PH', 'Phone'), ('Ch', 'Chargers'), ('Ca', 'Cases'))


class Product(models.Model):
    name = models.CharField(max_length=120)

    category = models.CharField(max_length=2, choices=CAT)


class ProductVersion(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=50)

    base_product = models.ForeignKey(Product)


class ProductAndCount(models.Model):
    product = models.ForeignKey(ProductVersion)
    count = models.BigIntegerField()


class Cart(models.Model):
    products = models.ManyToManyField(ProductAndCount)


class Order(models.Model):
    user = models.ForeignKey(User)
    products = models.ManyToManyField(ProductAndCount)
    delivery_address = models.CharField(max_length=300)
    delivery_date_and_time = models.DateTimeField()
