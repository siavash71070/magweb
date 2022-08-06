from django.urls import path
from django.contrib.auth import login, logout
from . import views



URLPatterns = [
    path('contact/submit/', views.contact_add, name='contact_add'),
    path('panel/contactform/', views.contact_show, name='contact_show'),
    path('panel/contactform/del/<str:pk>\d+/', views.contact_del, name='contact_del'),
 ]
 