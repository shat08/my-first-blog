from django.contrib import admin
from django.urls import path
from . import views

#app_name ="pdfmr"
#ここから追加


#ここまで



urlpatterns = [
    path('', views.top, name='top'),
    #path('top', views.top, name='top'),
    path('link', views.link, name='link'),#追加
    path('about', views.about, name='about'),#追加
    path('post', views.post, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    

    path('giants', views.giants, name='giants'),
    path('tigers', views.tigers, name='tigers'),
    path('baystars', views.baystars, name='baystars'),
    path('dragons', views.dragons, name='dragons'),
    path('carp', views.carp, name='carp'),
    path('swallows', views.swallows, name='swallows'),
    path('lions', views.lions, name='lions'),
    path('fighters', views.fighters, name='fighters'),
    path('marines', views.marines, name='marines'),
    path('hawks', views.hawks, name='hawks'),
    path('eagles', views.eagles, name='eagles'),
    path('buffaloes', views.buffaloes, name='buffaloes'),

    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),#追加
]