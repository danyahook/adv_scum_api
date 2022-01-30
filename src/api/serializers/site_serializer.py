from rest_framework import serializers

from api.models.site_model import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        read_only_fields = ('site_uuid', 'is_valid', 'is_approved', 'created_at')
        fields = '__all__'
