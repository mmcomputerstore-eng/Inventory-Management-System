import os
from functools import wraps
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
def connect_database(fx):
    @wraps(fx)
    def wraper(self,*args,**kwargs):
        try:
            self.db = sql.connect(host="localhost",user =os.getenv("user"),password = os.getenv("password"),database=os.getenv("database"))
            self.cursor = self.db.cursor()
            result = fx(self,*args,**kwargs)
            self.db.commit()
        except sql.Error:
            print("Faild to Connect Database...")
        except Exception as e :
            print(e)
            print("Un Known Error...")
        finally:
            if self.db.is_connected:
                self.cursor.close()
                self.db.close()

        return result
    return wraper


class Menu:
    def run(self):
        self.product= AddProduct()
        self.view = View()
        while True:
            print("=== Menu ===\n1. Add Product\n2. View All")
            try:
                choice = int(input("Enter option Number to contineu : "))
                if choice == 1:
                    self.product.add_products()
                elif choice == 2:
                    self.view.View_products()
            except ValueError:
                print("Please Eanter option Number like 1 for Add Product ...")
class AddProduct:
    @connect_database
    def add_products(self):
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
    @connect_database
    def View_products(self):
        self.cursor.execute("select * from products")
        data = self.cursor.fetchall()
        if not data:
            print('No Product Found in Record...')
        else:
            print("=== Products ===")
            for product in data:
                print(f"Product ID : {product[0]} | Name : {product[1]} | Price : {product[2]} | Stock : {product[4]}")
            print()


m = Menu()
m.run()