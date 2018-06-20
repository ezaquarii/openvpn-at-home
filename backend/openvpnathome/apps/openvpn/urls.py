from django.urls import path, re_path
from .api import ServerApi, ClientApi
from .views import DownloadServerConfig, DownloadClientConfig

api_urlpatterns = [
    path('servers/', ServerApi.as_view({'get': 'list', 'post': 'create'}), name='servers'),
    path('clients/', ClientApi.as_view({'get': 'list', 'post': 'create'}), name='clients'),
    path('clients/<int:id>/send/', ClientApi.as_view({'post': 'send_email'}), name='send-client-config'),
]

views_urlpatterns = [
    re_path('download/server/(?P<server_id>\d+)/(?P<filename>\w+\.conf$)', DownloadServerConfig.as_view(), name='download-server-config'),
    re_path('download/client/(?P<client_id>\d+)/(?P<filename>\w+\.ovpn$)', DownloadClientConfig.as_view(), name='download-client-config')
]
