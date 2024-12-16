import os
from django import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitroutine.settings')

application = get_asgi_application()