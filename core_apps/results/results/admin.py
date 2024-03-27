from django.contrib import admin
from .models import Results

from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)


class ResultsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "report", 
        # "player",
        "club_fk",
        "nickname_fk",
        "nickname",
        "nickname_id",
        "agents",
        "club",
        "profit_loss",
        "rake",
        "agent_deal",
        "agent_rb",
        "agent_adjustment",
        "agent_settlement",
        "player_deal_rb",
        "player_deal_adjustment",
        "player_rb",
        "player_adjustment",
        "player_settlement",
        "agent_earnings",
        "created_at",
        "updated_at"
        ]
    list_display_links = ["nickname"]
    # search_fields = ["user__username"]
    list_filter = [
        # ("Nickname_Player_User__Result_Nickname_Nickname__reportId__report_date",DateRangeFilterBuilder(title="Report date:")),
        ("report__report_date",DateRangeFilterBuilder(title="Report date:")),
        "nickname_fk__player"
        # "ref_currency"
    ]

admin.site.register(Results, ResultsAdmin)