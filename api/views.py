"""Views for api app"""

from django.conf import settings
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.request import Request

from api.models import VPS
from api.serializers import VPSSerializer


def get_param_or_zero(request: Request, param: str) -> str:
    """Return query parameter or 0 if it's None"""

    try:
        param = int(request.query_params.get(param) or '0')
    except (TypeError, AttributeError, ValueError):
        param = 0

    return int(param)


def get_param_or_max_int(request: Request, param):
    """Return query parameter or max positive integer if it's None"""

    try:
        param = int(request.query_params.get(param) \
            or settings.MAX_POSITIVE_INTEGER)
    except (TypeError, AttributeError, ValueError):
        param = settings.MAX_POSITIVE_INTEGER

    return int(param)


def get_vps_viewset_query_params(request: Request) -> dict:
    """Return query params from VPS viewset request"""

    try:
        query_params = {
            'status': request.query_params.get('status'),

            'cpu_from': get_param_or_zero(request, 'cpu_from'),
            'cpu_to': get_param_or_max_int(request, 'cpu_to'),

            'ram_from': get_param_or_zero(request, 'ram_from'),
            'ram_to': get_param_or_max_int(request, 'ram_to'),

            'hdd_from': get_param_or_zero(request, 'hdd_from'),
            'hdd_to': get_param_or_max_int(request, 'hdd_to'),
        }
    except AttributeError:
        query_params = None

    return query_params


class VPSPagination(PageNumberPagination):
    """Pagination for VPS viewset"""

    page_size = 20
    page_size_query_param = 'page_size'


class VPSViewSet(viewsets.ModelViewSet):
    """Viewset for VPS objects"""

    queryset = VPS.objects.all()

    # pagination_class = VPSPagination
    serializer_class = VPSSerializer

    def list(self, request: Request) -> Response:
        query_params = get_vps_viewset_query_params(request)

        if query_params:
            status = query_params['status']

            queryset = VPS.objects.filter(
                cpu__range=(query_params['cpu_from'], query_params['cpu_to']),
                ram__range=(query_params['ram_from'], query_params['ram_to']),
                hdd__range=(query_params['hdd_from'], query_params['hdd_to']),
            )

            if status:
                queryset = queryset.filter(status=status)
        else:
            queryset = VPS.objects.all()

        serializer = VPSSerializer(
            queryset, many=True, context={'request': request},
        )

        return Response(serializer.data)
