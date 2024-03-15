import pandas as pd

def uploadCSV(file):

    reader = pd.read_csv(file)

    for _, row in reader.iterrows():   

        club = row["CLUB"]
        nickname = row["NICKNAME"]   
        print(club) 