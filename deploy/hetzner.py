import os, sys

PROJECT_HOME = "/var/www/burgercom/"
# activate virtualenv
activate_this = os.path.expanduser("~/.virtualenvs/burgercom/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser(PROJECT_HOME))
os.environ['DJANGO_SETTINGS_MODULE'] = 'burgercom.settings_prod'
os.environ['DJANGO_SETTINGS_MODULE'] = 'burgercom.settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
