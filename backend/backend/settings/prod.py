from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# * production-specific configs here
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True