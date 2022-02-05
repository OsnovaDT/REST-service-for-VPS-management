"""Registration for models from api app"""

from django.contrib import admin

from api.models import VPS


@admin.register(VPS)
class VPSAdmin(admin.ModelAdmin):
    """Admin model for VPS"""

    list_display = ('uid', 'status', 'cpu', 'ram', 'hdd',)
    list_filter = ('status',)
