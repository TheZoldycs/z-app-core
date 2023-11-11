import django
import os
from django.core.asgi import get_asgi_application
from channels.security.websocket import OriginValidator
django_asgi_app = get_asgi_application()

print("start channels")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vulnvision.settings')
django.setup()
# is populated before importing code that may import ORM models.
from channels.routing import ProtocolTypeRouter,URLRouter
from chat.routing import websocket_urlpatterns
from chat.middleware import TokenAuthMiddleWare

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': OriginValidator( TokenAuthMiddleWare(
    URLRouter(
      websocket_urlpatterns
    )),
    ["*"]),
    }) 