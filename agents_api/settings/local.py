from .base import *
from .base import env

environ.Env.read_env(os.path.join(ROOT_DIR, '.envs/.local')) 

DEBUG = env.bool("DJANGO_DEBUG")
SECRET_KEY = env("DJANGO_SECRET_KEY")

# ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# AWS configuration

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')


AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME') # - Enter your S3 bucket name HERE



# Django 4.2 > Storage configuration for S3
STORAGES = {
    
    # Media file (image) management

    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    
    # CSS and JS file management

    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        
    },
    
}

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False