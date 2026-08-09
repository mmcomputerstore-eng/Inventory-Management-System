import os
from dotenv import load_dotenv
import mysql.connector as sql
from functools import wraps
load_dotenv()

def connect_database(fx):
    @wraps(fx)
    def wraper(self,*args,**kwargs):
        result = None
        try:
            self.db = sql.connect(host="localhost",user =os.getenv("db_user"),password = os.getenv("db_password"),database=os.getenv("db_database"))
            self.cursor = self.db.cursor()
            result = fx(self,*args,**kwargs)
            self.db.commit()
        # except sql.Error:
        #     print("Faild to Connect Database...")
        except Exception as e :
            print(e)
            print("Un Known Error...")
        finally:
            if self.db.is_connected():
                self.cursor.close()
                self.db.close()
        if result is not None: 
            return result
    return wraper
class Database:
    @connect_database
    def create_database(self):
        self.cursor.execute("create database if not exists inventory_management")
        self.cursor.execute("use inventory_management")
        self.cursor.execute("create table if not exists  product_Category(ID int primary key auto_increment, Category_name varchar(50))")
        self.cursor.execute("create table if not exists product_Brand (ID int primary key auto_increment, Brand_name varchar(50))")
        self.cursor.execute("create table if not exists products (ID int primary key auto_increment,Product_name varchar(50) not null, Purchase_Price int,Sell_Price int ,Crunt_stock int,Minimum_stock int,Category_id int,Brand_id int,foreign key (Category_id)references product_Category(ID),foreign key (Brand_id)references product_Brand(ID))")
        self.cursor.execute("create table if not exists suppliers(id int primary key auto_increment, Name varchar(50),Email varchar(100),Phone varchar(30))")
        self.cursor.execute("create table if not exists customers(id int primary key auto_increment, Name varchar(50),Email varchar(100),Phone varchar(30))")
        self.cursor.execute("create table if not exists purchases(id int primary key auto_increment,supplier_id int,date date,Total int,foreign key (supplier_id) references suppliers(id))")
        self.cursor.execute("create table if not exists purchases_details(purchase_id int,product_id int, quantity int , price int ,foreign key (purchase_id)references purchases(id),foreign key (product_id) references products(id))")
        self.cursor.execute("create table if not exists sales(id int primary key auto_increment,customer_id int,date date,Total int,foreign key (customer_id) references customers(id))")
        self.cursor.execute("create table if not exists sales_details(sales_id int primary key,product_id int, quantity int , price int ,foreign key (sales_id)references sales(id),foreign key (product_id) references products(id))")
        print("d")
