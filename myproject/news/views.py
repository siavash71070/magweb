from django.shortcuts import render,get_object_or_404,redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
import random
from comment.models import Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from itertools import chain



mysearch = ""


# Create your views here.

def news_detail(request,word):
     
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat =SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('show')

    popnews2 = News.objects.all().order_by('show')[:3]

    shownews = News.objects.filter(name=word)
    tagname = News.objects.get(name=word).tag
    tag = tagname.split(',')
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't Add Show ")

    code = News.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id=code, status=1).order_by('-pk')[:3]
    cmcount = len(comment)
    link ="/urls/" + str(News.objects.get(name=word).rand)

    return render(request,'front/news_detail.html', {"site":site,"news":news,"cat":cat,"subcat":subcat, "lastnews":lastnews,'shownews':shownews,'popnews':popnews,'popnews2':popnews2,'tag':tag,'trending':trending,'code':code,'comment':comment,'cmcount':cmcount,'link':link})



def news_detail_short(request,pk):
     
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat =SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('show')

    popnews2 = News.objects.all().order_by('show')[:3]

    shownews = News.objects.filter(rand=pk)
    tagname = News.objects.get(rand=pk).tag
    tag = tagname.split(',')
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't Add Show ")

    link ="/urls/" + str(News.objects.get(name=word).rand)

    return render(request,'front/news_detail.html', {"site":site,"news":news,"cat":cat,"subcat":subcat, "lastnews":lastnews,'shownews':shownews,'popnews':popnews,'popnews2':popnews2,'tag':tag,'trending':trending,'link':link,'tagname':tagname})

    

def news_list(request):

    
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end


    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser':
            perm = 1
            
    if perm == 0:

        news = News.objects.filter(Writer=request.user)
    elif perm == 1:
        newss = News.objects.all()
        paginator = Paginator(newss,2)
        page = request.GET.get('page')

        try:
            
            news = paginator.page(page)

        except EmptyPage:

            news = paginator.page(paginator.num_pages)

        except PageNotAnInteger :

            news = paginator.page(1)


    return render(request,'back/news_list.html',{'news':news})


def news_add(request):

    
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end

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


    date = str(year) + str(month) + str(day)
    randint = str(random.randint(1000,9999))
    rand = date + randint
    rand = int(rand)

    while len(News.objects.filter(rand=rand)) != 0 :

        randint = str(random.randint(1000,9999))
        rand = date + randint
        rand = int(rand)


    cat = SubCat.objects.all()
    

    if request.method == "POST":
        
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Requirded "
            return render(request,'back/error.html',{'error':error})
        try:

            myfile = request.FILES['myfile']
            fs =FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            url = fs.url(filename)
            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid

                    b = News(name=newstitle,short_text=newstxtshort,body_text=newstxt, date=today,picname=filename,picurl=url,Writer=request.user,catname=newsname,catid=newsid,show=0,time=time,ocatid=ocatid,tag=tag,rand=rand)
                    b.save()
                    count = len(News.objects.filter(ocatid=ocatid))

                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()


                    return redirect('news_list')
                else:
                    error = "Your File IS Bigger Than 5 MB "
                    return render(request,'back/error.html',{'error':error}) 
            else:
                fs = FileSystemStorage()
                fs.delete(filename)


                error = "Your File Not Supported "
                return render(request,'back/error.html',{'error':error}) 

        except:
            error = "Please Input Your Image "
            return render(request,'back/error.html',{'error':error})
    return render(request,'back/news_add.html',{'cat':cat})

def news_delete(request,pk):

    
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end


    
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser':
            perm = 1
            
    if perm == 0:

        a = News.objects.get(pk=pk).Writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request,'back/error.html',{'error':error})



    try:
        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)
        ocatid = News.objects.get(pk=pk).ocatid

        b.delete()

        
        count = len(News.objects.filter(ocatid=ocatid))

        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()

    except:
        error = " Something Is Wrong "
        return render(request,'back/error.html',{'error':error})


    return redirect("news_list")


def news_edit(request,pk):

    
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end

    

    if News.objects.get(pk=pk) == 0:
        error = " News Not Found "
        return render(request,'back/error.html',{'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser':
            perm = 1
            
    if perm == 0:

        a = News.objects.get(pk=pk).Writer
        if str(a) != str(request.user) :
            error = "Access Denied"
            return render(request,'back/error.html',{'error':error})




    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()

    
    if request.method == "POST":
        
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Requirded "
            return render(request,'back/error.html',{'error':error})
        try:

            myfile = request.FILES['myfile']
            fs =FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            url = fs.url(filename)
            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk=newsid).name
                    

                    b = News.objects.get(pk=pk)

                    
                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag
                    b.act = 0

                    b.save()
                    return redirect('news_list')
                else:
                    error = "Your File IS Bigger Than 5 MB "
                    return render(request,'back/error.html',{'error':error}) 
            else:
                fs = FileSystemStorage()
                fs.delete(filename)


                error = "Your File Not Supported "
                return render(request,'back/error.html',{'error':error}) 

        except:

           
            newsname = SubCat.objects.get(pk=newsid).name
            

            b = News.objects.get(pk=pk)

                    
            
            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            
            b.catname = newsname
            b.catid = newsid
            b.tag = tag

            b.save()
            
            return redirect('news_list')
   

    

    return render(request,'back/news_edit.html',{'pk':pk ,'news':news,'cat':cat})




def news_publish(request,pk):

    
    #login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login chck end

    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()

    return redirect("news_list")


def news_all_show(request,word):

    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ocatid=catid)

    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat =SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('show')
    popnews2 = News.objects.filter(act=1).order_by('show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]

    paginator = Paginator(allnews,12)
    page = request.GET.get('page')
    try:
        allnews = paginator.page(page)

    except EmptyPage:

        allnews = paginator.page(paginator.num_pages)

    except PageNotAnInteger:

        allnews = paginator.page(1)

    
    return render(request,'front/all_news.html', {"site":site,"news":news,"cat":cat,"subcat":subcat, "lastnews":lastnews,'popnews':popnews,'popnews2':popnews2,'trending':trending,'lastnews2':lastnews2,'allnews':allnews})


    

def all_news(request):

    allnews = News.objects.all()

    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat =SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('show')
    popnews2 = News.objects.filter(act=1).order_by('show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]

    paginator = Paginator(allnews,12)
    page = request.GET.get('page')
    try:
        allnews = paginator.page(page)

    except EmptyPage:

        allnews = paginator.page(paginator.num_pages)

    except PageNotAnInteger:

        allnews = paginator.page(1)

    
    return render(request,'front/all_news_2.html', {"site":site,"news":news,"cat":cat,"subcat":subcat, "lastnews":lastnews,'popnews':popnews,'popnews2':popnews2,'trending':trending,'lastnews2':lastnews2,'allnews':allnews})

def all_news_search(request):

    if request.method =='POST' :

        txt = request.POST.get('txt')
        mysearch = txt

        a = News.objects.filter(name__contains=txt)
        b = News.objects.filter(short_text__contains=txt)
        c = News.objects.filter(body_text__contains=txt)

        allnews = list(chain(a,b,c))
        allnews = list(dict.fromkeys(allnews))

    else:

        a = News.objects.filter(name__contains=mysearch)
        b = News.objects.filter(short_text__contains=mysearch)
        c = News.objects.filter(body_text__contains=mysearch)

        allnews = list(chain(a,b,c))
        allnews = list(dict.fromkeys(allnews))



    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat =SubCat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('show')
    popnews2 = News.objects.filter(act=1).order_by('show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]

    paginator = Paginator(allnews,12)
    page = request.GET.get('page')
    try:
        allnews = paginator.page(page)

    except EmptyPage:

        allnews = paginator.page(paginator.num_pages)

    except PageNotAnInteger:

        allnews = paginator.page(1)

    
    return render(request,'front/all_news_2.html', {"site":site,"news":news,"cat":cat,"subcat":subcat, "lastnews":lastnews,'popnews':popnews,'popnews2':popnews2,'trending':trending,'lastnews2':lastnews2,'allnews':allnews})





