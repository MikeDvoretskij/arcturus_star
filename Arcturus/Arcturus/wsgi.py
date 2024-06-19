import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/.../.../.../.../public_html/Arcturus') # <--------
#путь к фреймворку
sys.path.insert(0, '/.../.../.../.../public_html/Arcturus/Arcturus') # <--------
#путь к виртуальному окружению
sys.path.insert(0, '/.../.../.../.../venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3])) # <--------
os.environ["DJANGO_SETTINGS_MODULE"] = "Arcturus.settings"

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Arcturus.settings')

application = get_wsgi_application()
