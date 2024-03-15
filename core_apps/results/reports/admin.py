from django.contrib import admin
from .models import Reports

class ReportsAdmin(admin.ModelAdmin):
    list_display = [ "id", "agent","report_date"]
    list_display_links = ["report_date"]
    # search_fields = ["user__username"]

admin.site.register(Reports, ReportsAdmin)