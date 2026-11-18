
"""
ASGI config for CrewAI Django Hiring Assistant.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "crewai_django_hiring_assistant.config.settings"
)

application = get_asgi_application()
