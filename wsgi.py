import sys
import os

path = '/home/ivan/Escritorio/blog_back'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_APP'] = 'blog_back/app.py'

from app import app as application
