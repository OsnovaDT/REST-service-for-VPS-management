"""Serializers of api application"""

from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import VPS


class VPSSerializer(HyperlinkedModelSerializer):
    """Hyperlinked serializer for VPS model"""

    class Meta:
        """Info about the serializer"""

        model = VPS

        fields = (
            'uid', 'url', 'cpu',
            'ram', 'hdd', 'status',
        )
