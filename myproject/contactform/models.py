from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contactform(models.Model):

    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    txt = models.TextField()
    date =models.CharField(max_length=12,default="")
    time =models.CharField(max_length=12,default="")
    

    def __str__(self) :
        return self.name  
