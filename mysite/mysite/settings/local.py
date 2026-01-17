from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-gn)9k(2!h%4-^(=@obv_rvcifb5g-!6@r--thx0f^!beqs-ta4'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': 'blog123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = 'angelika.pawluk94@gmail.com'
EMAIL_HOST_PASSWORD = 'ryotyhjehsnfgeqn'