from django.conf.urls import url,path
from django.contrib.auth import login, logout
from . import views

from django.contrib.sitemaps.views import sitemap
from main.sitemap import MyNewsSiteMap


sitemap = {

    'news':MyNewsSiteMap(),
}





URLPatterns = [
    path('',views.home,name='home'),
    
    path('sitemap\.xml', sitemap, {'sitemap':sitemap}, name='django.contrib.sitemaps.views.sitemap'),

    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.myregister, name='myregister'),
    path('answer/comments/<int:pk>/', views.answer_cm, name='answer_cm'),

 ]