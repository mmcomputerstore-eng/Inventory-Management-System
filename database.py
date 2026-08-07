import os
from dotenv import load_dotenv
import mysql.connector as sql
load_dotenv()
db = sql.connect(host="localhost",user =os.getenv("user"),password = os.getenv("password"))
if db.is_connected:
    cursor = db.cursor()
    cursor.execute("create database if not exists inventory_management")
    cursor.execute("use inventory_management")
    cursor.execute("create table if not exists  product_Category(ID int primary key auto_increment, Category_name varchar(50))")
    cursor.execute("create table if not exists product_Brand (ID int primary key auto_increment, Brand_name varchar(50))")
    cursor.execute("create table if not exists products (ID int primary key auto_increment,Product_name varchar(50) not null, Purchase_Price int,Sell_Price int ,Crunt_stock int,Minimum_stock int,Category_id int,Brand_id int,foreign key (Category_id)references product_Category(ID),foreign key (Brand_id)references product_Brand(ID))")
    cursor.execute("create table if not exists suppliers(id int primary key auto_increment, Name varchar(50),Email varchar(100),Phone varchar(30))")
    cursor.execute("create table if not exists customers(id int primary key auto_increment, Name varchar(50),Email varchar(100),Phone varchar(30))")
    cursor.execute("create table if not exists purchases(id int primary key auto_increment,supplier_id int,date date,Total int,foreign key (supplier_id) references suppliers(id))")
    cursor.execute("create table if not exists purchases_details(purchase_id int primary key,product_id int, quantity int , price int ,foreign key (purchase_id)references purchases(id),foreign key (product_id) references products(id))")
    cursor.execute("create table if not exists sales(id int primary key auto_increment,customer_id int,date date,Total int,foreign key (customer_id) references customers(id))")
    cursor.execute("create table if not exists sales_details(sales_id int primary key,product_id int, quantity int , price int ,foreign key (sales_id)references sales(id),foreign key (product_id) references products(id))")