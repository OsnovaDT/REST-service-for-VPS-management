"""Views for api app"""

from rest_framework import viewsets

from api.models import VPS
from api.serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    """Viewset for VPS objects"""

    queryset = VPS.objects.all()

    serializer_class = VPSSerializer
