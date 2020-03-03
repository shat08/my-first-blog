from django.contrib import admin
from django.urls import path
from . import views

app_name ="pdfmr"
#ここから追加


#ここまで



urlpatterns = [
    path('', views.top, name='top'),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),#追加
]