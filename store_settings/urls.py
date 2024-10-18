from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settings_view, name='settings'),  # URL for the settings page
]
