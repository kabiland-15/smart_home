import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from authenticate import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartHome.settings")

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": URLRouter(
            routing.websocket_urlpatterns
        ),
    }
)
