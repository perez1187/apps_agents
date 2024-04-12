from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")), 

    path("api/agent/", include("core_apps.results.agents.urls")), 
    path("api/user/", include("core_apps.users.profiles.urls")),
    path("api/reports/", include("core_apps.results.reports.urls")), 
    path("api/deals/", include("core_apps.results.deals.urls")),
    path("api/settlements/", include("core_apps.settlements.urls")),

    path("api/scripts/user/", include("core_apps.scripts.user_scripts.urls")),
    path("api/scripts/nickname/", include("core_apps.scripts.nickname_scripts.urls")),
    path("api/scripts/result/", include("core_apps.scripts.result_scripts.urls")),
    path("api/scripts/settlemets/", include("core_apps.scripts.settlements_script.urls")),

    path("api/views/agents-summary/", include("view_apps.agents_summary.urls")),
    path("api/views/agents-reports/", include("view_apps.agents_reports.urls")),
    path("api/views/agents-deals/", include("view_apps.agents_deals.urls")),
    # path("api/views/agents-settlements/", include("view_apps.agents_deals.urls")),
    path("api/views/agents-player-results/", include("view_apps.agents_player_results.urls")),
    path("api/views/agents-settings/", include("view_apps.agents_settings.urls")),
    path("api/views/agents-settlements/", include("view_apps.agents_settlements.urls")),

    path("api/views/player-deals/", include("view_apps.player_deals.urls")),
    path("api/views/player-player-results/", include("view_apps.player_player_results.urls")),
    path("api/views/player-player-settings/", include("view_apps.player_player_settings.urls")),
    path("api/views/player-settlements/", include("view_apps.player_player_settlements.urls")),
    path("api/views/player-reports/", include("view_apps.player_reports.urls")),
    path("api/views/player-summary/", include("view_apps.player_summary.urls")),

    path("api/views/players-deals/", include("view_apps.players_deals.urls")),
    path("api/views/players-player-results/", include("view_apps.players_player_results.urls")),
    path("api/views/players-player-settings/", include("view_apps.players_settings.urls")),
    path("api/views/players-player-settlements/", include("view_apps.players_settlements.urls")),
    path("api/views/players-reports/", include("view_apps.players_reports.urls")),
    path("api/views/players-summary/", include("view_apps.players_summary.urls")),     



]

admin.site.site_header = "app accounts"
admin.site.site_title = "app accounts"
admin.site.index_title = "app accounts"