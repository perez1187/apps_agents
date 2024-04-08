import requests
import pandas as pd


def create_account(username, password):
    url = 'http://127.0.0.1:8000/api/v1/auth/users/'
    myobj = {
        "username":username,
        "password":password
    } 
    x = requests.post(url, json = myobj)

    print(f'username {username} {x}')

def upload_csv():
    df = pd.read_csv(r"usernames.csv")
    # print(df)
    for _,row in df.iterrows():
        username = row["username"]
        password = row["pass"]

        create_account(username, password)
        # print(username)


# # url = 'https://www.w3schools.com/python/demopage.php'
# url = 'http://127.0.0.1:8000/api/v1/auth/users/'
# # myobj = {'somekey': 'somevalue'}
# myobj = {
# 	"username":"player67",
# 	"password":"0321b82a-420d-4379-a60a-9f802f8ff164"
# }

# x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

# print(x)
 
   
    # for nickname in nicknames_qs:
    #     record_key = f'{nickname["club"]}{nickname["nickname"]}{nickname["nickname_id"]}'
    #     record_value = nickname["id"]

    #     nicknames_dict[record_key]= record_value


# test = {}

# test["a"]={
#     "id":5,
#     "name":"chuj"
# }
# print(test["a"]["id"])

if __name__ == "__main__":

    upload_csv()