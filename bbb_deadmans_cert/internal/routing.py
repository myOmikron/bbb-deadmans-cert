from django.urls import re_path

from internal.consumers import Heartbeat

websocket_urlpatterns = [
    re_path(r'deadman/internal/ws/test', Heartbeat.as_asgi()),
]
