import pandas as pd
import logging
import decimal

from django.contrib.auth import get_user_model
User = get_user_model()

from core_apps.users.profiles.models import Profile
# from core_apps.results.results.models import Results


logger = logging.getLogger(__name__)

def createUsers(reader):

    for _,row in reader.iterrows():
        username = row["username"]
        password = row["pass"]

        # print(username + "" + password)
        User.objects.create(
            username=username,
            password=password
        )
        logger.info(f"user {username} was created")

def addAdminToUsername(reader):

    for _,row in reader.iterrows():
        username = row["username"]
        agent = row["agent"]

        objUser= User.objects.get(
            username=username
        )
        objAgent=User.objects.get(
            username=agent
        )

        objProfile = Profile.objects.get(
            user=objUser.pk
        )
        objProfile.agent = objAgent
        objProfile.save()

        logger.info(f"agent {agent} was added to user {username} profile")

def uploadCSV(file, request):
  
    reader = pd.read_csv(file)
    createUsers(reader)
    addAdminToUsername(reader)