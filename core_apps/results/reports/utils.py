import pandas as pd
import logging

from core_apps.results.deals.models import Nicknames
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
        record_key = f'{nickname["club"]}{nickname["nickname"]}{nickname["nickname_id"]}'
        record_value =  {
            "id":nickname["id"],
            
        }
        
        

        nicknames_dict[record_key]= record_value


    for _,row in file.iterrows():
        record_key = f'{row["CLUB"]}{row["NICKNAME"]}{row["PLAYERS"]}'

        if record_key in nicknames_dict:
            continue

        nickname_obj = Nicknames.objects.create(
            agent=agent,
            agents=row["AGENTS"],
            nickname=row["NICKNAME"],
            nickname_id=row["PLAYERS"],
            club=row["CLUB"]
        )

        nicknames_dict[record_key]=nickname_obj.pk
        logger.info(f"agent: {agent}: {row['NICKNAME']} Nickname was created")   
        
        return nicknames_dict

def uploadCSV(file, request):

    reader = pd.read_csv(file)
    # print(request.user)
    
    # report_dict = dict_report_dates(reader, request.user)
    # print(report_dict)

    nicknames_dict = dict_nicknames(reader, request.user)



    # for _, row in reader.iterrows():   

    #     club = row["CLUB"]
    #     nickname = row["NICKNAME"]   
    #     print(club) 