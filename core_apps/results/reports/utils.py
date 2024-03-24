import pandas as pd
import logging
import decimal

from core_apps.results.deals.models import Nicknames
from core_apps.results.results.models import Results
from .models import Reports

logger = logging.getLogger(__name__)

def ref_dict(df, currency_dict):
    
    # create dict for cashe
    ref_dict = {}

    refs = df['REF'].unique()

    # fetching all refs
    ref_qs = models.Ref.objects.all().values()
    
    # adding ref to cashe
    for c in ref_qs:
        try:
            ref_dict[c['ref_name']] = c['id']  
        except:
            continue

    # find or creaate currency from agent currency
    for ref in refs:

        if ref not in ref_dict:

            # add currency to DB
            obj_ref = models.Ref.objects.create(
                ref_name=ref
            )

            # add currency to dict(cashe)
            ref_dict[ref]=obj_ref.pk
            logger.info(f"{ref} Ref was created")    
    
    return ref_dict

def dict_report_dates(file, agent):
    '''
    fetch file 
    fetch agent reports from db and create dict
    if in the file the is no date, date= today
    check if reports exists in db (date, agent)
    if not, create report and add to dict
    return dict of reports
    '''

    report_dict = {}
    # reports_from_file = file['CLUB'].unique()
    # print(reports_from_file)
    # print(agent)




    ''' 
        for MVP only report today
    '''
    report_obj = Reports.objects.create(
        agent=agent,    
    )
    report_dict["today"]= report_obj.pk
    return report_dict

def dict_nicknames(file, agent):
    '''
    fetch file 
    fetch agent nicknames from db and create dict
    check if nickname exists in db (nickname, club)
    if not, create nickname and add to dict
    return dict of nicknames
    '''    

    nicknames_dict = {}
    nicknames_qs = Nicknames.objects.filter(agent=agent).values()

    for nickname in nicknames_qs:
        record_key = f'{nickname["club"]}{nickname["nickname"]}'
        record_value = {
            "id":nickname["id"],
            "rb":nickname["rb"],
            "rebate":nickname["rebate"]
        }

        nicknames_dict[record_key]= record_value
        

    for _,row in file.iterrows():
        record_key = f'{row["CLUB"]}{row["NICKNAME"]}'

        if record_key in nicknames_dict:
            continue

        nickname_obj = Nicknames.objects.create(
            agent=agent,
            agents=row["AGENTS"],
            nickname=row["NICKNAME"],
            nickname_id=row["PLAYERS"],
            club=row["CLUB"]
        )

        nicknames_dict[record_key]= {
            "id":nickname_obj.pk,
            "rb":0,
            "rebate":0
        }     
        
        logger.info(f"agent: {agent}: {row['NICKNAME']} Nickname was created")   
        
    return nicknames_dict

def uploadCSV(file, request):

    reader = pd.read_csv(file)
    
    ''' 
    for mvp only 1 report,
    key: ["today]
    value: id
    '''
    # tworzy raporty ( po dacie)
    # pobiera nicki, ew dodaje nowe
    #  

    report_dict = dict_report_dates(reader, request.user)
    
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
                

    # for _, row in reader.iterrows():   

    #     club = row["CLUB"]
    #     nickname = row["NICKNAME"]   
    #     print(club) 