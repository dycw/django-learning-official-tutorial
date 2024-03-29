"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from typing import Any

from django.core.asgi import get_asgi_application


_ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application: Any = get_asgi_application()
