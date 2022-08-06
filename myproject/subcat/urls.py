from django.urls import path
from . import views


urlpatterns = [

    path(r'^panel/subcategory/list/$', views.subcat_list, name='subcat_list'),
    path(r'^panel/subcategory/add/$', views.subcat_add, name='subcat_add'),

]