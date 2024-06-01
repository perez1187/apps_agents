from django.contrib import admin
from .models import Results
from django.http import HttpResponse
import csv


from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)


def export_results(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "report", 
        # "CLUB",
        "player",
        "nickname",
        "nickname_id",
        # 
        "club",
        "agent_settlement",
        "profit_loss",
        "rake",
        "agent_deal",
        "agent_rb",        
        "agent_adjustment",                
        ])
    results = queryset.values_list(
        "report__report_date", 
        "nickname_fk__player__username",
        "nickname",
        "nickname_id",
        "club",
        "agent_settlement",
        "profit_loss",
        "rake",
        "agent_deal",
        "agent_rb",        
        "agent_adjustment", 

        )

    for result in results:
        writer.writerow(result)

    return response
export_results.short_description = 'Export Results to csv'   


class ResultsAdmin(admin.ModelAdmin):

    def player(self,obj):
        # if obj._player_settlement == None:
        #     return 0

        return obj.nickname_fk.player



    list_display = [
        "id",
        "report", 
        # "player",
        "club_fk",
        "player",
        "nickname_fk",
        "nickname",
        "nickname_id",
        "agents",
        "club",
        "player_settlement",
        "agent_settlement",
        "agent_earnings",
        "profit_loss",
        "rake",
        "agent_deal",
        "agent_rb",        
        "agent_adjustment",                
        "player_deal_rb",
        "player_deal_adjustment",
        "player_rb",
        "player_adjustment",
        "player_settlement",
        "created_at",
        "updated_at"
        ]
    list_display_links = ["nickname"]
    actions = [export_results]
    list_per_page = 20
    search_fields = ["nickname","nickname_fk__player__username"]
    search_by=[
        "Nickname and Player",
    ]    
    search_help_text = f'Search by: {", ".join(search_by)}'  
    list_filter = [
        # ("Nickname_Player_User__Result_Nickname_Nickname__reportId__report_date",DateRangeFilterBuilder(title="Report date:")),
        ("report__report_date",DateRangeFilterBuilder(title="Report date:")),
        "nickname_fk__player"
        # "ref_currency"
    ]

admin.site.register(Results, ResultsAdmin)