# myapp/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Microcontroller  # Replace with your actual model


class MicrocontrollerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Microcontroller.objects.all()  # Replace with your model

    def lastmod(self, obj):
        return obj.updated_at  # Use the last modified date field 


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["home", "all_microcontrollers", "all_microcontrollers"]

    def location(self, item):
        return reverse(item)
