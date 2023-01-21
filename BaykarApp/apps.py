from django.apps import AppConfig

# Set app name and default auto-increment type.

class BaykarappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaykarApp'
