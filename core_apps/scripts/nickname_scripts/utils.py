import pandas as pd
import logging
import decimal

from django.contrib.auth import get_user_model
User = get_user_model()

from core_apps.users.profiles.models import Profile
# from core_apps.results.results.models import Results


logger = logging.getLogger(__name__)

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

def dict_usernames(agent):

    user_dict = {}
    user_qs = User.objects.filter(profile__agent=agent.pk)

    print(user_qs)
    for u in user_qs:
        print(u)

def uploadCSV(file, request):
  
    reader = pd.read_csv(file)

    agent = request.user  

    dict_users=dict_usernames(agent)
    
    
    # dict_nicknames = dict_nicknames(reader,agent)
    # for _,row in reader.iterrows():    
    #     nickname = row["nickname"]
    #     club= row["club"]
    #     rb = row["rb"]
    #     rebate= row["adj"]

        # print(nickname + club + str(rb) + str(rebate))