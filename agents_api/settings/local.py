from .base import *
from .base import env



DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env(
#     "DJANGO_SECRET_KEY",
#     default="django-insecure-^^1-!d(40!4hivk#xl&c-s=cg_812sh8p$p7_q-om8n)&c=rdp",
# )
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]