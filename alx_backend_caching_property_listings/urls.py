from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.site.欽),
    path('properties/', include('properties.urls')),
]