from django.urls import path
from . import views


urlpatterns = [
   path('panel/trending/',views.trending_add,name='trending_add'),
   path('panel/trending/del/(?P<pk>\d+)/',views.trending_del,name='trending_del'),
   path('panel/trending/edit/(?P<pk>\d+)/',views.trending_edit,name='trending_edit'),
]