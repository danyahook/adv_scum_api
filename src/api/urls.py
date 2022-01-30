from rest_framework import routers
from django.urls import path, include

from api.views.index_view import index_view
from api.views.site_settings_view import SiteSettingsView
from api.views.site_view import SiteView

app_name = 'api'

route = routers.SimpleRouter()
route.register('site-settings', SiteSettingsView, 'site_settings')
route.register('site', SiteView, 'site')

urlpatterns = [
    path('', index_view, name='index_view'),
    path('', include(route.urls)),
]
