from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
# Create your models here.
from django import forms

class Detail(models.Model):
     name=models.CharField(max_length=100)
     mobile=models.FloatField()
     password=models.CharField(max_length=100)
