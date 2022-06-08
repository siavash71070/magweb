from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Main(models.Model):

    name = models.CharField(max_length= 30)
    about = models.TextField()
    abouttxt = models.TextField(default="")
    fb = models.CharField(default="-",max_length= 60)
    yt = models.CharField(default="-",max_length= 60)
    tw = models.CharField(default="-",max_length= 60)
    Tell = models.CharField(default="-",max_length= 30)
    Link = models.CharField(default="-",max_length= 30)
    insta = models.CharField(default="-",max_length= 60)

    seo_txt = models.CharField(default="-",max_length= 200)
    seo_keywords = models.TextField(default="-")

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    set_name= models.CharField(default="-",max_length= 30) 

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    def __str__(self) :
        return self.set_name + " | "  +  str(self.pk)  
