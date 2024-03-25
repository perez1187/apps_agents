from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.results.reports.models import Reports
from core_apps.results.deals.models import Nicknames
from core_apps.results.deals.models import Clubs

class Results(models.Model):

    report =  models.ForeignKey(
        Reports,
        on_delete=models.CASCADE,
        verbose_name=_("Report"),
        related_name='results_report',  
    )
    nickname_fk =  models.ForeignKey(
        Nicknames,
        on_delete=models.CASCADE,
        verbose_name=_("Nickname FK"),
        related_name='results_nickname',  
    )  
    club_fk =  models.ForeignKey(
        Nicknames,
        on_delete=models.CASCADE,
        verbose_name=_("Club FK"),
        related_name='results_club',  
        blank=True,
        null=True
    )        
    
    # nickname fk
    # club 
    club = models.CharField(
        verbose_name=_("Club"), 
        max_length=40, 
        blank=True,
        null=True
    ) 
    nickname_id = models.CharField(
        verbose_name=_("Nickname"), 
        max_length=40, 
        blank=True,
        null=True
    )    
    nickname = models.CharField(
        verbose_name=_("Nickname"), 
        max_length=40, 
        blank=True,
        null=True
    )    
    agents = models.CharField(
        verbose_name=_("App Agent"), 
        max_length=40, 
        blank=True,
        null=True
    )    
    profit_loss =  models.DecimalField(
        verbose_name=_("Profit Loss"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )
    rake =  models.DecimalField(
        verbose_name=_("Rake"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )    
    agent_deal =  models.DecimalField(
        verbose_name=_("Deal"),
        max_digits=6, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    ) 
    agent_rb =  models.DecimalField(
        verbose_name=_("RB"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )      
    agent_adjustment =  models.DecimalField(
        verbose_name=_("Adjustment"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    ) 
    agent_settlement =  models.DecimalField(
        verbose_name=_("Agent settlement"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )
    player_deal_rb =  models.DecimalField(
        verbose_name=_("Player Deal RB"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )   
    player_deal_adjustment =  models.DecimalField(
        verbose_name=_("Player Deal Adjustment"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )      
       
    player_rb =  models.DecimalField(
        verbose_name=_("Player RB"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )    
    player_adjustment =  models.DecimalField(
        verbose_name=_("Player adjustment"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )    
    player_settlement =  models.DecimalField(
        verbose_name=_("Player settlement"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )
    agent_earnings =  models.DecimalField(
        verbose_name=_("Agent earn"),
        max_digits=15, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        default=00.000,
    )    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )                 

