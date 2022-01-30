from rest_framework import viewsets

from api.serializers.site_serializer import SiteSerializer

from api.models.site_model import Site


class SiteView(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
