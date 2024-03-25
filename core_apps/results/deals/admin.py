from django.contrib import admin
from .models import Nicknames, Clubs

class NicknamesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "agent", 
        "player",
        "nickname",
        "nickname_id",
        "club",
        "rb",
        "rebate",
        "created_at",
        "updated_at"
        ]
    list_display_links = ["nickname"]
    search_fields = ["nickname"]

admin.site.register(Nicknames, NicknamesAdmin)

class ClubsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "club"
        ]
    list_display_links = ["club"]
    search_fields = ["club"]

admin.site.register(Clubs, ClubsAdmin)