"""
WSGI config for jhre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# WSGI is a specification that describes how a web server communicates 
# with web applications and how web applications can be chained together to process a request
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jhre.settings')

application = get_wsgi_application()
