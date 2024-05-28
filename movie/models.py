#import the models module from django.db. This module helps to define and map 
#the characteristics of the model into the database

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='movie/image/')
    url=models.URLField(blank=True)#. Because not all movies have URLs, we specify blank=True to indicate that this #field is optional
    def __str__(self) :
        return self.title
class Review(models.Model):
    text=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain=models.BooleanField()
    #Returns the review text when the review object is printed or displayed.
    def __str__(self) :
        return self.text



# Create your models here.
