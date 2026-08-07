import os
from functools import wraps
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
def connectdatabase(fx):
    @wraps(fx)
    def wraper(self,*args,**kwargs):
        self.db = sql.connect(host="localhost",user =os.getenv("user"),password = os.getenv("password"),database=os.getenv("database"))
        self.cursor = self.db.cursor()
        result = fx(self,*args,**kwargs)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return result
    return wraper


class Menu:
    def __init__(self):
        self.product= Addproduct()
        self.view = View()
        while True:
            print("=== Menu ===\n1. Add Product\n2. View All")
            try:
                a = int(input("Enter option Number to contineu : "))
                if a == 1:
                    self.product.Add()
                elif a == 2:
                    self.view.View()
            except ValueError:
                print("Please Eanter option Number like 1 for Add Product ...")
class Addproduct:
    @connectdatabase
    def Add(self):
        name = input("Eanter Product Name : ")
        self.cursor.execute("select * from products where product_name = %s",(name,))
        data = self.cursor.fetchone()
        if data ==None:
            while True:
                try:
                    price = int(input(f"Eanter {name} Price : "))
                    break
                except ValueError:
                    print("Please Eanter Price in Numbers...")
            while True:
                try:
                    stock = int(input(f"Eanter {name} Stock / Quantity : "))
                    break
                except ValueError:
                    print("Please Eanter Stock in Numbers...")
            self.cursor.execute("insert into products (product_name,Purchase_Price,Crunt_Stock) values (%s,%s,%s)",(name,price,stock))
            print(f"Product Name {name} Add successfully in Database...")
        else:
            print(f"product Name {name} Already Found in Record with product ID {data[0]} Dublicate Product Not Allowed...")

class View:
    @connectdatabase
    def View(self):
        self.cursor.execute("select * from products")
        data = self.cursor.fetchall()
        if data == None:
            print('No Product Found in Record...')
        else:
            print("=== Products ===")
            for product in data:
                print(f"Product ID : {product[0]} | Name : {product[1]} | Price : {product[2]} | Stock : {product[4]}")
            print()


m = Menu()