"""Routing of the api application"""

from django.urls import path, include
from rest_framework import routers

from api.views import VPSViewSet


api_router = routers.DefaultRouter()

api_router.register('vps', VPSViewSet)


urlpatterns = [
    path('', include(api_router.urls),),
]
