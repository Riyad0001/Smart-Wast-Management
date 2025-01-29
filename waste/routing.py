from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/waste_bins/$', consumers.WasteBinConsumer.as_asgi()),
]