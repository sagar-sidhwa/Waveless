from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.
class Admin(models.Model):
    users = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    users = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Farmer(models.Model):
    users = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

class Customer(models.Model):
    users = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

class Categorydata(models.Model):

    category= models.CharField(max_length=50)
    heading= models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    img = models.ImageField()
    e = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.category

class Productdata(models.Model):

    heading= models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price= models.FloatField(max_length=15)
    img = models.ImageField()
    c = models.ForeignKey(Categorydata, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title