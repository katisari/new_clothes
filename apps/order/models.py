from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    cart_users = models.ManyToManyField(User, related_name="cart_items")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Photo(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    desc = models.TextField()
    item = models.ForeignKey(Item, related_name="photos", null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# class Order(models.Model):
#     number = models.IntegerField()
#     user = models.ForeignKey(User, related_name = "orders")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class Cart(models.Model):

    
