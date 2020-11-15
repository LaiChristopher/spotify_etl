import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker 
import requests
import json 
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqllite://my_played_tracks.sqlite"
USER_ID = "christopher.lai"
TOKEN = "BQDt8JjFrMRATXV8ZNaKYL3v9HYaK4NDbAB0aM2MUkIb9pmwmbHyPu-PV_4OkXHs-PFxpXcMBCb9ElMIdLnKYpAD-n3Dtf0SJbw6YV5Hs9qYQxoJ1NUJ6c4OeMfm0XE0HhzaKo4PfuSrJatpKLOO5ccSmIw"

if __name__ == "__main__":

    # Extract part of the ETL process

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    # Convert time to Unix timestamp in miliseconds      
    today = datetime.datetime.now()
    yesterday = today -datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000


    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()
    
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object  
    for song in data[items]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"]
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

   


