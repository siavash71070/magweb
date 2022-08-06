
from blacklist.views import black_list, ip_add, ip_del
from django.urls import include, path
#from django.conf.urls import include, url
from django.contrib import admin
from news.views import all_news, all_news_search, news_detail_short, news_list,news_add
from main.views import about_setting, answer_cm, change_pass, contact, home, about, mylogin, mylogout, myregister, panel, show_data,site_setting
from django.conf import settings
from django.conf.urls.static import static
from cat.views import cat_add, cat_list
from subcat.views import subcat_add, subcat_list
from contactform.views import contact_add, contact_del, contact_show
from trending.views import trending_add
from manager.views import add_users_to_group, del_users_to_group, groups_perms, groups_perms_add, manager_group_add, groups_perms_del, manager_del, manager_group, manager_group_add, manager_group_del, manager_list, manager_perms, manager_perms_add, manager_perms_del, users_group,add_users_to_group, users_perms, users_perms_add, users_perms_del
from newsletter.views import check_mychecklist, news_emails, news_letter, news_phones, news_txt_del, send_email
from comment.views import comments_confirme, comments_del, comments_list, news_add_cm
from django .views.static import serve
from django.conf import settings


from django.contrib.sitemaps.views import sitemap
from main.sitemap import MyNewsSiteMap


from rest_framework import routers
from main import views


router = routers.DefaultRouter()
router.register(r'mynews',views.NewsViewSet )

sitemaps = {

    'news':MyNewsSiteMap(),
}

urlpatterns =[

    path('admin/',admin.site.urls),

    path('rest/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

    path(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


    path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    path('static/(?P<path>.*)',serve,{'document_root':settings.STATIC_ROOT}),


    path('',home,name='home'),
    #path('', include('newsletter.urls')),
    path('about/', about, name='about'),
    path('news/', include('news.urls')),
    path('panel/', panel, name='panel'),
    path('panel/panel/news/list/',news_list,name='news_list'),
    path('panel/panel/news/add/',news_add,name='news_add'),
    path('cat/', include('cat.urls')),
    path('panel/panel/category/list/', cat_list, name='cat_list'),
    path('panel/panel/category/add/', cat_add, name='cat_add'),
    path('subcat/', include('subcat.urls')),
    path('panel/panel/subcategory/list/', subcat_list, name='subcat_list'),
    path('panel/panel/subcategory/add/', subcat_add, name='subcat_add'),
    path('login/', mylogin, name='mylogin'),
    path('logout/', mylogout, name='mylogout'),
    path('panel/setting', site_setting, name='site_setting'),
    path('panel/about/setting', about_setting, name='about_setting'),
    path('contact/', contact, name='contact'),
    #path('contacform/', include('contactform.urls')),
    path('contact/submit/', contact_add, name='contact_add'),
    path('panel/contactform/',contact_show, name='contact_show'),
    path('panel/contactform/del/<str:pk>\d+/', contact_del, name='contact_del'),
    path('trending/', include('trending.urls')),
    path('panel/trending/',trending_add,name='trending_add'),
    path('panel/panel/change/pass/',change_pass,name='change_pass'),
    path('register/', myregister , name='myregister'),
    #path('manager/',include('manager.urls'))
    path('panel/panel/manager/list', manager_list,name='manager_list'),
    path('panel/manager/del/<str:pk>\d+/',manager_del, name='manager_del'),
    path('panel/panel/manager/group', manager_group,name='manager_group'),
    path('panel/panel/manager/perms', manager_perms,name='manager_perms'),
    path('panel/panel/manager/group/add', manager_group_add,name='manager_group_add'),
    path('panel/manager/group/del/<str:name>.*/', manager_group_del, name='manager_group_del'),
    path('panel/manager/group/show/<int:pk>/', users_group, name='users_group'),
    path('panel/manager/perms/show/<int:pk>/', users_perms, name='users_perms'),
    path('panel/manager/addtogroup/<int:pk>/', add_users_to_group, name='add_users_to_group'),
    path('panel/manager/deltogroup/<int:pk>/<str:name>.*/', del_users_to_group, name='del_users_to_group'),
    path('panel/manager/perms/del/<str:name>.*/', manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add/', manager_perms_add, name='manager_perms_add'),
    path('panel/manager/delperm/<int:pk>/<str:name>.*/', users_perms_del, name='users_perms_del'),
    path('panel/manager/addperm/<int:pk>/', users_perms_add, name='users_perms_add'),
    path('panel/manager/addpermtogroup/<str:name>.*/', groups_perms, name='groups_perms'),
    path('panel/manager/group/delperms/<str:gname>.*/<str:name>.*/', groups_perms_del, name='groups_perms_del'),
    path('panel/manager/group/addperms/<str:name>/', groups_perms_add, name='groups_perms_add'),
    path('newsletter/add',news_letter,name='news_letter'),
    path('panel/panel/newsletter/emails',news_emails,name='news_emails'),
    path('panel/panel/newsletter/phones',news_phones,name='news_phones'),
    path('panel/panel/newsletter/del/<int:pk>/<int:num>/',news_txt_del,name='news_txt_del'),
    path('urls/<int:pk>/', news_detail_short, name='news_detail_short'),
    #path('comment',include('comment.urls'))
    path('comment/add/news/<int:pk>/',news_add_cm, name='news_add_cm'),
    path('comments/list/',comments_list, name='comments_list'),
    path('comments/del/<int:pk>/',comments_del, name='comments_del'),
    path('comments/confirme/<int:pk>/',comments_confirme, name='comments_confirme'),
    path('blacklist/',black_list,name='black_list'),
    path('blacklist/add/',ip_add,name='ip_add'),
    path('blacklist/del/<int:pk>/',ip_del,name='ip_del'),
    path('answer/comments/<int:pk>/', answer_cm, name='answer_cm'),
    path('send/email/',send_email,name='send_email'),
    path('all/news/', all_news, name='all_news'),
    path('/search/', all_news_search, name='all_news_search'),
    path('check/checklist/',check_mychecklist,name='check_mychecklist'),
    path('show/data/', show_data, name='show_data'),
    
]

    
    



if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

