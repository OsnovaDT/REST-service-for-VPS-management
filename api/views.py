"""Views for api application"""

from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from api.models import VPS
from api.serializers import VPSSerializer
from api.constants import ERRORS_IN_GETTING_PARAMETER, MAX_POSITIVE_INTEGER


def get_param_or_zero(request: Request, param: str) -> int:
    """Return query parameter or 0 if it's None"""

    try:
        param = int(request.query_params.get(param) or 0)
    except ERRORS_IN_GETTING_PARAMETER:
        param = 0

    return int(param)


def get_param_or_max_int(request: Request, param: str) -> int:
    """Return query parameter or max positive integer if it's None"""

    try:
        param = int(request.query_params.get(param) or MAX_POSITIVE_INTEGER)
    except ERRORS_IN_GETTING_PARAMETER:
        param = MAX_POSITIVE_INTEGER

    return int(param)


def get_vps_query_params(request: Request) -> dict | None:
    """Return query params for VPS viewset"""

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


def get_vps_queryset_by_query_params(query_params: dict) -> QuerySet:
    """Return queryset for VPS by query params"""

    queryset = VPS.objects.filter(
        cpu__range=(query_params['cpu_from'], query_params['cpu_to']),
        ram__range=(query_params['ram_from'], query_params['ram_to']),
        hdd__range=(query_params['hdd_from'], query_params['hdd_to']),
    )

    status = query_params['status']

    if status:
        queryset = queryset.filter(status=status)

    return queryset


class VPSViewSet(ModelViewSet):
    """Viewset for VPS objects"""

    queryset = VPS.objects.all()
    serializer_class = VPSSerializer

    def list(self, request: Request) -> Response:
        query_params = get_vps_query_params(request)

        if query_params:
            queryset = get_vps_queryset_by_query_params(query_params)
        else:
            queryset = VPS.objects.all()

        serializer = VPSSerializer(
            queryset, many=True, context={'request': request},
        )

        return Response(serializer.data)
