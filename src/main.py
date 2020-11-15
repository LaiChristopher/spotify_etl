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
TOKEN = "BQAiyUClE_UbWyenBbCZPdSMGniL-Nua6O6lKjJS4s6Zi1dZjls4sHhVcCS_CNKlbLoUnA97x_vmuu7hKvSbj7Urt2F6wPA6ssoVtMHqwJskI3YHJOoekaYo5NJ3KOytH5oCykBlnyg1RijXcfP-8V7_xmk"

if __name__ = "__main__":

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json"
        "Authorization" : "Bearer {to"
    }