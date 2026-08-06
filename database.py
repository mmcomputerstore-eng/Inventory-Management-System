import os
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
db = sql.connect(host="localhost",user =os.getenv("user"),password = os.getenv("password"))
if db.is_connected:
    print("Counected")