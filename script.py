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




if __name__ == "__main__":

    upload_csv()