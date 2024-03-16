from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
# import datetime


User = get_user_model()

class Nicknames(models.Model):
    agent =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Agent"),
        related_name='deal_agent',  
    )
    player =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Player"),
        related_name='deal_player', 
        blank=True,
        null=True 
    )    
 
    nickname = models.CharField(
        verbose_name=_("Nickname"), 
        max_length=40, 
    )

    nickname_id = models.CharField(
        verbose_name=_("Nickname"), 
        max_length=40, 
        default="",
        blank=True, 
        null=True
    )
    club = models.CharField(
        verbose_name=_("Club"), 
        max_length=40, 
    )
    rb = models.DecimalField(
        verbose_name=_("Rakeback"),
        max_digits=6, 
        decimal_places=2, 
        null=False, 
        blank=False, 
        default=00.00)  

    rebate = models.DecimalField(
        verbose_name=_("Rebate"),
        max_digits=6, 
        decimal_places=2, 
        null=False, 
        blank=False, 
        default=00.00)                  

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )     
    def __str__(self):
        return self.nickname  
