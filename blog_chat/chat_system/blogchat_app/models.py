from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class NavbarModel(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    navbar_logo = models.CharField(max_length=100,null=True, blank=True)

class PostModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.CharField(max_length=300,null=True,blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True)
    image = models.ImageField(upload_to='images_uploaded',null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField(auto_now=True)

class LogoModel(models.Model):
    logo_image = models.ImageField(upload_to = 'logo_uploaded',null = True, blank = True)
    logo_url = models.URLField(null = True, blank = True)

class AboutModel(models.Model):
    headimage = models.ImageField(upload_to='aboutimage_uploaded',null=True,blank=True)
    title = models.CharField(max_length=100,null=True, blank=True)
    text = models.CharField(max_length=400,null=True, blank=True)
    ownimage = models.ImageField(upload_to='aboutimage_uploaded',null=True,blank=True)
    name = models.CharField(max_length=40,null=True, blank=True)
    profession = models.CharField(max_length=40,null=True, blank=True)
    small_inf = models.CharField(max_length=100,null=True, blank=True)

# class ContactModel(models.Model):
#     d = models.CharField()

# class ContactModel2(models.Model):
#     active = models.
#     adreess = models