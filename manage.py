import os
from django.core.management import execute_from_command_line
from django.core.asgi import get_asgi_application  # Use ASGI for serverless environments

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    execute_from_command_line()
else:
    # Vercel expects an `app` callable
    app = get_asgi_application()