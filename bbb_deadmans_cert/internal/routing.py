from django.urls import re_path

from internal.consumers import Heartbeat

websocket_urlpatterns = [
    re_path(r'deadman/internal/ws/subscribe', Heartbeat.as_asgi()),
]
