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

    path("api/scripts/user/", include("core_apps.scripts.user_scripts.urls")),
    path("api/scripts/nickname/", include("core_apps.scripts.nickname_scripts.urls")),
    path("api/scripts/result/", include("core_apps.scripts.result_scripts.urls")),

    path("api/views/agents-summary/", include("view_apps.agents_summary.urls")),
    path("api/views/agents-reports/", include("view_apps.agents_reports.urls")),
]

admin.site.site_header = "app accounts"
admin.site.site_title = "app accounts"
admin.site.index_title = "app accounts"