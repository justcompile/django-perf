from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=20)
    store = models.ForeignKey(Store)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    store = models.ForeignKey(Store)

    categories = models.ManyToManyField(Category)


class Image(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, related_name='images')


class Order(models.Model):
    total = models.DecimalField(decimal_places=2, max_digits=6)
    order_date = models.DateTimeField()

    customer = models.ForeignKey(User)
    store = models.ForeignKey(Store)


class OrderLine(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, related_name='order_lines')
