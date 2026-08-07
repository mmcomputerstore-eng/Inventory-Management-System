import os
from functools import wraps
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
def connectdatabase(fx,*args,**kwargs):
    @wraps(fx)
    def wraper(fx,*args,**kwargs):
        db = sql.connect(host="localhost",user =os.getenv("user"),password = os.getenv("password"),database=os.getenv("database"))
        cursor = db.cursor()
        result = fx(*args,**kwargs)
        cursor.close()
        db.close()
        return result
    return wraper


class Menu:
    def __init__(self):
        self.product= Addproduct()
        while True:
            print("=== Menu ===\n1. Add Product")
            try:
                a = int(input("Enter option Number to contineu : "))
            except ValueError:
                print("Please Eanter option Number like 1 for Add Product ...")
