from django.contrib import admin

from api.models.site_model import Site
from api.models.site_settings_model import SiteSettings

admin.site.register(Site)
admin.site.register(SiteSettings)
