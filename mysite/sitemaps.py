from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from pdfmr.models import Post


class StaticViewSitemap(Sitemap):
    """
    静的ページのサイトマップ
    """
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['pdfmr:top']

    def location(self, item):
        return reverse(item)