from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import resolve_url
from django.urls import path, include
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return resolve_url('blog:detail', pk=obj.pk)

    def lastmod(self, obj):
        return obj.created_at


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
    path('', include('pdfmr.urls')),
]