from django.urls import path
from django.contrib.auth import login, logout
from . import views



URLPatterns = [
    path('panel/manager/list/',views.manager_list, name='manager_list'),
    path('panel/manager/del/<str:pk>\d+/', views.manager_del, name='manager_del'),
    path('panel/manager/group/',views.manager_group, name='manager_group'),
    path('panel/panel/manager/group/add', views.manager_group_add,name='manager_group_add'),
    path('panel/manager/addtogroup/<int:pk>/', views.add_users_to_group, name='add_users_to_group'),
 ]