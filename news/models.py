from django.db import models
class News(models.Model):
    headline=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField()
    #call python  __str__  method to return string representation of object
    def __str__(self):
        return self.headline


# Create your models here.
