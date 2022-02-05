"""Views for api app"""

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.models import VPS
from api.serializers import VPSSerializer


class VPSPagination(PageNumberPagination):
    """Pagination for VPS viewset"""

    page_size = 20
    page_size_query_param = 'page_size'


class VPSViewSet(viewsets.ModelViewSet):
    """Viewset for VPS objects"""

    queryset = VPS.objects.all()

    pagination_class = VPSPagination
    serializer_class = VPSSerializer
