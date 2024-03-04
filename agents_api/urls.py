from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "app accounts"
admin.site.site_title = "app accounts"
admin.site.index_title = "app accounts"