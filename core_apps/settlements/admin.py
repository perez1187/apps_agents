from django.contrib import admin

from . import models

from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

class SettlementAdmin(admin.ModelAdmin):

    def Date_Trans(self, obj):

        if obj.date == None:
            return ""

        return obj.date.strftime("%Y-%m-%d")

    list_display = [
        "agent",
        "player",
        # "date", 
        "Date_Trans",
        "transactionUSD",
        "transactionValue",
        "currency",
        "exchangeRate",
        "description",
        "created_at",
        "updated_at"
        ]
    list_display_links = ["player"]
    search_fields = ["player__username"]
    search_by=[
        "Player Username",
    ]    
    search_help_text = f'Search by: {", ".join(search_by)}'    
    list_filter = [
        ("date",DateRangeFilterBuilder(title="Transaction Date:")),
        # "player"
    ]
    ordering= ("-date",)

admin.site.register(models.Settlement, SettlementAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'currency',
    ]
    list_display_links = ['currency']

admin.site.register(models.Currency, CurrencyAdmin)    