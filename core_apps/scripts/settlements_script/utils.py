import pandas as pd
import logging
import decimal

from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import status

from core_apps.settlements.models import Currency, Settlement

from .exceptions import TemplateExcpetion

logger = logging.getLogger(__name__)


def uploadCSV(file, request):

    reader = pd.read_csv(file)

    reader["exc rate"] = reader["exc rate"].fillna(0)
    
    for _,row in reader.iterrows():

        agent = row["agent"]
        player = row["player"]
        date = row["date"]
        transactionUSD=row["trans usd"]
        transactionValue=row["trans value"]
        currency= row["currency"]
        exchangeRate=row["exc rate"]
        description=row["description"]

        

        agent_fk = User.objects.get(username= agent)
        player_fk=User.objects.get(username=player)
        currency_get_or_create = Currency.objects.get_or_create(
            currency=currency
        )
        currency_fk=Currency.objects.get(currency=currency)
        # print(agent_fk)
        # print(currency_fk)
        # print(player)
        # print(player_fk)
        # print(date)
        # print(type(exchangeRate))

        if exchangeRate == "nan":
            exchangeRate=0

        Settlement.objects.create(
            agent=agent_fk,
            player=player_fk,
            date=date,
            transactionUSD=transactionUSD,
            transactionValue=transactionValue,
            exchangeRate=exchangeRate,
            currency=currency_fk,
            description=description
        )
        # print("created")
