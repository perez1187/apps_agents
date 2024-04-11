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
    search_fields = [
        "nickname",
        "club",
        "player"
        ]
    search_fields = ["nickname","club"]
    search_by=[
        "Nickname,Club and Player",
    ] 
    search_help_text = f'Search by: {", ".join(search_by)}'           

admin.site.register(Nicknames, NicknamesAdmin)

class ClubsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "club"
        ]
    list_display_links = ["club"]
    search_fields = ["club"]
    

admin.site.register(Clubs, ClubsAdmin)