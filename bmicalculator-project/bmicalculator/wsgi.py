"""
WSGI config for bmicalculator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# Martin Quinn 24-01-2019
# PTA18070

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bmicalculator.settings')

application = get_wsgi_application()
