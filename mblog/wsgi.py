# 專案資料夾/mblog/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
import sys

path = "/home/casper50206/mblog/"

if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

application = get_wsgi_application()