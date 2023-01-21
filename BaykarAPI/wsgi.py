import os
from django.core.wsgi import get_wsgi_application

# Define environment settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BaykarAPI.settings')

# Note about WSGI : Web Server Gateway Interface (WSGI) is a specification that describes 
# the communication between web servers and Python web applications or frameworks.
application = get_wsgi_application()
