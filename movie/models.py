#import the models module from django.db. This module helps to define and map 
#the characteristics of the model into the database

from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='movie/image/')
    url=models.URLField(blank=True)#. Because not all movies have URLs, we specify blank=True to indicate that this 
#field is optional


# Create your models here.
