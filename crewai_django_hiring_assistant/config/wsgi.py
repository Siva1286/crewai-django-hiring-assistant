
"""
WSGI config for CrewAI Django Hiring Assistant.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "crewai_django_hiring_assistant.config.settings"
)

application = get_wsgi_application()
