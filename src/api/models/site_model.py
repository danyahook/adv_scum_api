import uuid

from django.db import models

from api.models.site_settings_model import SiteSettings


class Site(models.Model):
    site_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.URLField(unique=True)
    is_valid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, related_name='settings', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
