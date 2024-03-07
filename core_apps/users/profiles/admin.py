from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = [ "id", "user","about_user"]
    list_display_links = ["id"]
    search_fields = ["user__username"]

admin.site.register(Profile, ProfileAdmin)