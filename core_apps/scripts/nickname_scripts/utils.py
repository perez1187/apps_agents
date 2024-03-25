import pandas as pd
import logging
import decimal

from django.contrib.auth import get_user_model
User = get_user_model()

from core_apps.users.profiles.models import Profile
from core_apps.results.deals.models import Nicknames
from core_apps.results.deals.models import Clubs
# from core_apps.results.results.models import Results


logger = logging.getLogger(__name__)


def dict_usernames(agent):

    user_dict = {}
    user_qs = User.objects.filter(profile__agent=agent.pk)

    for user in user_qs:

        user_dict[str(user)]=user.pk
    
    return user_dict

def club_dict(df):

    clubs_dict  = {}
    clubs_unique = df['club'].unique()
    club_qs = Clubs.objects.all().values()

    for club in club_qs:
        clubs_dict[club["club"]] = club["id"] 
        # print(club)

    for c in clubs_unique:
        if c in clubs_dict:
            continue
        club_obj = Clubs.objects.create(
            club=c
        )

        logger.info(f"club {c} was created")
    logger.info(f"return club dict")
    return clubs_dict

def uploadCSV(file, request):
  
    reader = pd.read_csv(file)

    agent = request.user  

    dict_users=dict_usernames(agent)
    dict_club = club_dict(reader)
    # print(reader)
    return
    df1 = reader.drop_duplicates(subset=["nickname","club"])
    # print(df1)
    # return

    # print(dict_users)
    
    # dict_nicknames = dict_nicknames(reader,agent)
    for _,row in df1.iterrows():    
        nickname = row["nickname"]
        club= row["club"]
        rb = row["rb"]
        rebate= row["adj"]
        player = row["player"]

        # try:
        #     nickname_id = row["nickname_id"]
        # # except DatabaseError as db_err:
        # #     logger.exception("Report error here.")
        # #     raise db_err            
        # except Exception:
        #     nickname_id = "0"

        # print(dict_users[player])
        # try:
        Nicknames.objects.create(
            agent=agent,
            player_id=dict_users[player],
            nickname=nickname,
            # nickname_id=nickname_id,
            club=club,
            rb=rb,
            rebate=rebate
        )
        # except DatabaseError as db_err:
        #     logger.exception("Report error here.")
        #     raise db_err            
        # except Exception:
        #     logger.exception(f"WARNING nickname: {nickname} and club {club} already exist")
        
        logger.info(f"nickname: {nickname} - was created")

        # print(nickname + club + str(rb) + str(rebate))