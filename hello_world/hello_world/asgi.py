"""
ASGI config for hello_world project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
# 和 asgi 兼容的 web 服务入口，可以方便的运行项目

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world.settings')

application = get_asgi_application()
