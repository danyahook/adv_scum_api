from rest_framework import serializers

from api.models.site_model import Site

from api.serializers.site_settings_serializer import SiteSettingsSerializer


class SiteSerializer(serializers.ModelSerializer):
    settings = SiteSettingsSerializer()

    class Meta:
        model = Site
        read_only_fields = ('site_uuid', 'is_valid', 'is_approved', 'created_at')
        fields = ('id', 'site_uuid', 'name', 'is_valid', 'is_approved', 'settings', 'created_at')
