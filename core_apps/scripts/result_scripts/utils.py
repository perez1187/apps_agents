import pandas as pd
import logging
import decimal

from core_apps.results.deals.models import Nicknames
from core_apps.results.results.models import Results
from core_apps.results.reports.models import Reports
# from .models import Reports

logger = logging.getLogger(__name__)


def dict_report_dates(df, agent):
    '''
    fetch file 
    fetch agent reports from db and create dict
    if in the file the is no date, date= today
    check if reports exists in db (date, agent)
    if not, create report and add to dict
    return dict of reports
    '''

    report_dict = {}
    report_date = df['DATE'].unique()
    reports_qs = Reports.objects.filter(
        agent=agent
    ).values()

    # print(reports_qs)
    example_date = "2024-03-24"

    for d in reports_qs:
        date = str(d["report_date"])

        report_dict[date] = d["id"]

    for date in report_date:
        if date in report_dict:
            continue
        

    # print(report_dict)
    # if example_date in report_dict:
    #     print("dziala")
    # else:
    #     print("nie")

    # report_obj = Reports.objects.create(
    #     agent=agent,    
    # )
    # report_dict["today"]= report_obj.pk
    return report_dict


def uploadCSV(file, request):

    reader = pd.read_csv(file)

    # tworzy raporty ( po dacie)
    # pobiera nicki, ew dodaje nowe
    #  

    report_dict = dict_report_dates(reader, request.user)
    return    
    # print(report_dict)

    nicknames_dict = dict_nicknames(reader, request.user)

    for _,row in reader.iterrows():
        nickname_fk = f'{row["CLUB"]}{row["NICKNAME"]}'  
        player_rb = decimal.Decimal(row["RAKE"])*decimal.Decimal(nicknames_dict[nickname_fk]["rb"])
        player_adj = (decimal.Decimal(row["PROFIT/LOSS"]) + player_rb) * decimal.Decimal(nicknames_dict[nickname_fk]["rebate"])

        # print(row["CLUB"])
        result_obj = Results.objects.create(
            # metadata
            report_id=report_dict["today"],
            nickname_fk_id=nicknames_dict[nickname_fk]["id"],
            club=row["CLUB"],
            nickname_id=row["PLAYERS"],
            nickname=row["NICKNAME"],
            agents=row["AGENTS"],

            # player and agent results
            profit_loss=row["PROFIT/LOSS"],
            rake= row["RAKE"],

            agent_deal=row["DEAL"],
            agent_rb=row["RAKEBACK"],
            agent_adjustment=row["ADJUSTMENT"],
            agent_settlement=row["AGENT SETTLEMENT"],

            # player deal
            player_deal_rb=nicknames_dict[nickname_fk]["rb"],
            player_deal_adjustment=nicknames_dict[nickname_fk]["rebate"],

            player_rb=player_rb,
            player_adjustment=player_adj,
            player_settlement= decimal.Decimal(row["PROFIT/LOSS"]) + player_rb - player_adj,

            agent_earnings =decimal.Decimal(row["AGENT SETTLEMENT"]) - decimal.Decimal(row["PROFIT/LOSS"]) + player_rb - player_adj,

        )
        logger.info(f"result {result_obj.pk} was created")   