from django.shortcuts import render,get_object_or_404,redirect
from.models import Blacklist
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User,Group,Permission
from manager.models import Manager
import random
import string
import datetime


# Create your views here.

def black_list(request) :

    ip = Blacklist.objects.all()

    return render(request,'back/black_list.html',{'ip':ip})


def ip_add(request) :

    if request.method == 'POST' :
        ip = request.POST.get('ip')

        if ip != "":
            b = Blacklist(ip=ip)
            b.save()


    return redirect('black_list')


def ip_del(request,pk) :


    b = Blacklist.objects.filter(pk=pk)
    b.delete()

    return redirect('black_list')

