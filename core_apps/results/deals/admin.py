from django.contrib import admin
from .models import Nicknames, Clubs
from django.http import HttpResponse
import csv

def export_nicknames(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nicknames.csv"'
    writer = csv.writer(response)
    
    writer.writerow([
        "nickname",
        "club",
        "rb",
        "adj",
        "player"            
        ])
    nicknames = queryset.values_list(
        "nickname",
        "club",
        "rb",
        "rebate",
        "player__username"

        )

    for nickname in nicknames:
        writer.writerow(nickname)

    return response
export_nicknames.short_description = 'Export Nicknames to csv'   

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
    actions = [export_nicknames]
    list_filter = [
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