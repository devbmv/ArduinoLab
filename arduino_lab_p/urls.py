"""arduino_lab_p URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from errors.errors_view import (
    handler404,
    handler403,
    handler500,
    handler400,
)  # Import the error handlers

from products.sitemaps import MicrocontrollerSitemap, StaticViewSitemap

# Define the sitemaps dictionary
sitemaps = {
    "microcontrollers": MicrocontrollerSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", include("home.urls")),  # Include URLs from home app
    path("admin/", admin.site.urls),  # Admin site
    path("accounts/", include("allauth.urls")),  # Authentication (allauth)
    path("products/", include("products.urls")),  # Product app URLs
    path("bag/", include("bag.urls")),  # Shopping bag app URLs
    path("checkout/", include("checkout.urls")),  # Checkout process
    path("profile/", include("profiles.urls")),  # User profile URLs
    path("store_settings/", include("store_settings.urls")),  # Store settings 
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),  # Sitemap URL
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # Serving media files
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)  # Serving static files

# Register the error handlers
handler404 = "errors.errors_view.handler404"
handler403 = "errors.errors_view.handler403"
handler500 = "errors.errors_view.handler500"
handler400 = "errors.errors_view.handler400"
