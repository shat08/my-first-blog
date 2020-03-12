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
    path('top', include('pdfmr.urls')),
    path('link', include('pdfmr.urls')),#追加
    path('about', include('pdfmr.urls')),#追加
    path('post', include('pdfmr.urls')),#追加

    path('giants',include('pdfmr.urls')),
    path('tigers',include('pdfmr.urls')),
    path('baystars',include('pdfmr.urls')),
    path('dragons',include('pdfmr.urls')),
    path('carp',include('pdfmr.urls')),
    path('swallows',include('pdfmr.urls')),
    path('lions',include('pdfmr.urls')),
    path('buffaloes',include('pdfmr.urls')),
    path('fighters',include('pdfmr.urls')),
    path('marines',include('pdfmr.urls')),
    path('hawks',include('pdfmr.urls')),
    path('eagles',include('pdfmr.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
]