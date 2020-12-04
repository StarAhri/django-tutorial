"""
WSGI config for hello_world project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# 与 wsgi 兼容的 web 服务的入口

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world.settings')

application = get_wsgi_application()
