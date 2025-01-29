import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import waste.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waste_management.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            waste.routing.websocket_urlpatterns
        )
    ),
})