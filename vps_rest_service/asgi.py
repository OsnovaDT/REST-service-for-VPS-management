"""ASGI config of the project"""

from os import environ

from django.core.asgi import get_asgi_application


environ.setdefault('DJANGO_SETTINGS_MODULE', 'vps_rest_service.settings')

application = get_asgi_application()
