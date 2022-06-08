from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('<str:word>/', views.news_detail, name='news_detail'),
    #url(r'^(?P<word>).*/$', views.news_detail, name='news_detail'),
    path('panel/news/list/', views.news_list, name='news_list'),
    path('panel/news/add/', views.news_add, name='news_add'),
    path('panel/news/del/<str:pk>\d+/', views.news_delete, name='news_delete'),
    path('panel/news/edit/<str:pk>\d+/', views.news_edit, name='news_edit'),
    path('panel/news/publish/<str:pk>\d+/', views.news_publish, name='news_publish'),
    path('urls/<int:pk>/', views.news_detail_short, name='news_detail_short'),
    path('all/news/<str:word>/', views.news_all_show, name='news_all_show'),
    path('all/news/', views.all_news, name='all_news'),

    
   
]