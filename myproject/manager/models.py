from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Manager(models.Model):

    name = models.CharField(max_length= 50)
    utxt = models.TextField()
    email = models.TextField(default="")
    ip = models.TextField(default="")
    country = models.TextField(default="")
    password = models.CharField(default="-",max_length=50)
   
    def __str__(self) :
        return self.name 
