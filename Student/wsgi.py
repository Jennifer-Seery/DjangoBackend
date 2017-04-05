## Exposes WSGI Module
##

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Student.settings")

##Creating self contained unit that can be deployed anywhere using whitenoise
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
