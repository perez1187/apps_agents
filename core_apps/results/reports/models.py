from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


User = get_user_model()

class Reports(models.Model):
    agent =  models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Agent"),
        related_name='report_agent',  
    )
    report_date = models.DateField(
        default=datetime.date.today, 
        db_index=True, 
        null=True, 
        blank=True 
    )    
    description = models.CharField(
        verbose_name=_("Description"), 
        max_length=1024, 
        default="", 
        null=True, 
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )     
    def __str__(self):
        return self.report_date.strftime("%Y-%m-%d")  
