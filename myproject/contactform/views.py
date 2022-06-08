from django.shortcuts import render,get_object_or_404,redirect
import datetime
from.models import Contactform
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage



# Create your views here.
def contact_add(request):


    
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    today = str(year)+"/"+str(month)+"/"+str(day)
    time = str(now.hour) +":"+str(now.minute)



    if request.method == 'POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        txt = request.POST.get('msg')

        if name == "" or email == "" or txt == "":

            msg = "All Fields Requirded "
            return render(request,'front/msgbox.html',{'msg':msg})

        b = Contactform(name=name,email=email,txt=txt,date=today,time=time)
        b.save()
        msg = "Your Massage Receved "
        return render(request,'front/msgbox.html',{'msg':msg})




    return render(request,'front/msgbox.html')

def contact_show(request):


    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end
    

    msg = Contactform.objects.all()


    return render(request,'back/contact_show.html',{'msg':msg})

def contact_del(request,pk):


    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end

    b = Contactform.objects.filter(pk=pk)
    b.delete()
    


    return redirect('contact_show')


