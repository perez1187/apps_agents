from django.contrib import admin
from .models import Nicknames

class NicknamesAdmin(admin.ModelAdmin):
    list_display = [
        "agent", 
        "player",
        "nickname",
        "club",
        "rb",
        "rebate",
        "created_at",
        "updated_at"
        ]
    list_display_links = ["nickname"]
    # search_fields = ["user__username"]

admin.site.register(Nicknames, NicknamesAdmin)