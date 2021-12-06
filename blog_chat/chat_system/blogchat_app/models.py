from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class PostModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.CharField(max_length=300,null=True,blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True)
    image = models.ImageField(upload_to='images_uploaded',null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField(auto_now=True)