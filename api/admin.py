"""Registering models from the api application"""

from django.contrib import admin

from api.models import VPS


@admin.register(VPS)
class VPSAdmin(admin.ModelAdmin):
    """Customize VPS model showing in the admin panel"""

    list_display = (
        'uid', 'status', 'cpu', 'ram', 'hdd',
    )

    list_filter = ('status',)
