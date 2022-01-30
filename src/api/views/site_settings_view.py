from rest_framework import viewsets

from api.serializers.site_settings_serializer import SiteSettingsSerializer

from api.models.site_settings_model import SiteSettings


class SiteSettingsView(viewsets.ModelViewSet):
    serializer_class = SiteSettingsSerializer
    queryset = SiteSettings.objects.all()
