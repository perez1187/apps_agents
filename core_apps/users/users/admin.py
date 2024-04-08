from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import OuterRef, Subquery, Sum, Count

from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

from .models import User, UserProxy

from core_apps.results.results.models import Results


class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    model = User
    list_display = [
        "pkid",
        "id",
        "username",
        "is_agent",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "username"]
    list_filter = ["username", "is_staff","is_agent"]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {"fields": ()},
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    'is_agent',
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ["username"]


admin.site.register(User, UserAdmin)

class UserProxyAdmin(admin.ModelAdmin):

    def get_queryset(self,request):

        from_date = request.GET.get('deal_player__results_nickname__report__report_date__range__gte','2010-01-01')
        to_date = request.GET.get('deal_player__results_nickname__report__report_date__range__lte','2100-01-01')        

        queryset = super(UserProxyAdmin, self).get_queryset(request)
        
        queryset = queryset.annotate(
           _player_settlement=Subquery(               
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))  
                .filter(report__report_date__range=[from_date,to_date])             
                .values("nickname_fk__player")
                .annotate(player_settlement=Sum("player_settlement"))
                .values("player_settlement")
             ),   
           _profit_loss_USD=Subquery(               
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))  
                .filter(report__report_date__range=[from_date,to_date])             
                .values("nickname_fk__player")
                .annotate(profit_loss=Sum("profit_loss"))
                .values("profit_loss")
             ),
            _rake_USD=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])
                .values("nickname_fk__player")
                .annotate(rake_USD=Sum("rake"))
                .values("rake_USD")
            ),
            _rb_USD=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(rb_USD=Sum("player_rb"))
                .values("rb_USD")
            ),
            _rebate_USD=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(rebate_USD=Sum("player_adjustment"))
                .values("rebate_USD")
            ),
            _agent_settlement_USD=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(agent_settlement_USD=Sum("agent_settlement"))
                .values("agent_settlement_USD")
            ),
            _agent_rb_USD=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(agent_rb_USD=Sum("agent_rb"))
                .values("agent_rb_USD")
            ),
            _agent_adj=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(agent_adj=Sum("agent_adjustment"))
                .values("agent_adj")
            ),   
            _agent_earn=Subquery(
                Results.objects.filter(nickname_fk__player=OuterRef("pk"))
                .filter(report__report_date__range=[from_date,to_date])                
                .values("nickname_fk__player")
                .annotate(agent_earn=Sum("agent_earnings"))
                .values("agent_earn")
            ),                                                                                        

        )

        return queryset

    def player_settlement(self,obj):
        if obj._player_settlement == None:
            return 0

        return "%.2f $" % obj._player_settlement

    def profit_loss(self,obj):
        if obj._profit_loss_USD == None:
            return 0

        return "%.2f $" % obj._profit_loss_USD        

    def rake(self,obj):
        if obj._rake_USD == None:
            return 0

        return "%.2f $" % obj._rake_USD

    def player_rb(self,obj):
        if obj._rb_USD == None:
            return 0

        return "%.2f $" % obj._rb_USD

    def player_adj(self,obj):
        if obj._rebate_USD == None:
            return 0
        res = obj._rebate_USD
        return "%.2f $" % res      

    def agent_settlement(self,obj):
        if obj._agent_settlement_USD == None:
            return 0

        return "%.2f $" % obj._agent_settlement_USD  
    
    def agent_rakeback(self,obj):
        if obj._agent_rb_USD == None:
            return 0

        return "%.2f $" % obj._agent_rb_USD     

    def agent_adj(self,obj):
        if obj._agent_adj == None:
            return 0

        return "%.2f $" % obj._agent_adj   
    
    def agent_earnings(self,obj):
        if obj._agent_earn == None:
            return 0

        return "%.2f $" % obj._agent_earn           

    # def player_all_settlement(self,obj):
    #     if obj._player_settlement == None:
    #         return 0

    #     return "%.2f $" % obj._player_settlement  


             
    ordering = ["username"]
    list_display = [
        # "pkid",
        # "id",
        "username",
        "player_settlement",
        "profit_loss",
        "rake",
        "player_rb",
        "player_adj",
        "agent_earnings",
        "agent_settlement",
        "agent_rakeback",
        "agent_adj"
        # "player_all_settlement",


    ]

    search_fields = [
        'username',
    ]

    search_fields_my_text = [

        "username"
    ]

    search_help_text = f'search in: {", ".join(search_fields_my_text)}' 

    list_filter = [
        # ("Nickname_Player_User__Result_Nickname_Nickname__reportId__report_date",DateRangeFilterBuilder(title="Report date:")),
        ("deal_player__results_nickname__report__report_date",DateRangeFilterBuilder(title="Report date:")),
        # "ref_currency"
    ]
admin.site.register(UserProxy, UserProxyAdmin)  