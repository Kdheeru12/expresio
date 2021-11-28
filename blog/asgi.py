"""
ASGI config for blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application_name = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import video_signalling.routing


application = ProtocolTypeRouter(
    {
        "http": application_name,
        "websocket": AuthMiddlewareStack(
            URLRouter(video_signalling.routing.websocket_urlpatterns)
        ),
    }
)