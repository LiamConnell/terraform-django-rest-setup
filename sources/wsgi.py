import os, sys

import logging
logger =logging.getLogger("")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)-8s %(messages)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

sys.stdout = sys.stderr
from os.path import abspath, dirname, join
import site

PROJECT_ROOT = abspath(join(dirname(__file__), "../pysrc"))
SETTINGS_LOC = abspath(join(PROJECT_ROOT, ''))
site.addsitedir(SETTINGS_LOC)
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

import django
django.setup()

sys.path.insert(0, join(PROJECT_ROOT, "apps"))

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
