from django.contrib import admin
from .models import Results

class ResultsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "report", 
        # "player",
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

admin.site.register(Results, ResultsAdmin)