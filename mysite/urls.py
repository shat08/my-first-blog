from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import resolve_url
from django.urls import path, include
from pdfmr.models import Post

app_name ="pdfmr"

from .sitemaps import (
    StaticViewSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdfmr.urls')),
   
    
    

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
]