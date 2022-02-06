"""Routing of the project"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(
        'admin/', admin.site.urls
    ),

    # Api authentication
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),

    # api application
    path(
        'api/', include('api.urls'),
    ),
]
