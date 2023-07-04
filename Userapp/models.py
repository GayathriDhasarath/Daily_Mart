from django.db import models
from Adminapp.models import *
from django.db.models.deletion import CASCADE


# Create your models here.
class Contact_details(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    subject=models.CharField(max_length=40)
    message=models.TextField(max_length=250)
    def __str__(self):
        return self.name
class Users_registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    Address=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class Cart(models.Model):
    userid=models.ForeignKey(Users_registration,on_delete=models.CASCADE)
    productid=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)
class Checkout(models.Model):
    userid=models.ForeignKey(Users_registration,on_delete=models.CASCADE)
    cartid=models.ForeignKey(Cart,on_delete=models.CASCADE)
    address=models.TextField(max_length=40)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=10)
    





