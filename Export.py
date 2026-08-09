from database import connect_database
import json
import csv

def export(self):
    file_name = input("Eanter file Name : ")
    while True:
        try:
            print("== Select File Formate ==\n1. Json\n2. CSV\n3. TXT")
            option = int(input("Eanter Option Number to contineu : "))
            if option == 1:
                json_file(self,file_name)
                break
            elif option == 2:
                csv_file(self,file_name)
                break
            elif option == 3:
                txt_file(self,file_name)
                break
            else:
                print("You Eanterd Invalid Option Please Try Again...")
        except ValueError:
            print("Please Eanter Option Number like (1) for Json...")

@connect_database
def product_data(self):
    self.cousor.execute("Select id,product_name,purchase_price,sell_price,crunt_stock from products")
    return self.cousor.fetchall()

def json_file(self,file_name):
    products = product_data(self)
    with open (file_name+".json","w",indent = 4) as file:
        for product in products:
            json.dump({
                "product id" : product[0],
                "product name" : product[1],
                "purchase price" : product[2],
                "sell price" : product[3],
                "crunt stock" : product[4]
            })

def csv_file(self,file_name):
    products = product_data(self)
    with open(file_name+".csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(["product id","product name","purchase price","sell price","crunt stock"])
        for product in product_data:
            writer.writerows([product[0],product[1],product[2],product[3],product[4]])

def txt_file(self,file_name):
    products = product_data(self)
    with open (file_name+".txt","w") as file:
        for product in products:
            file.write(f"product id : {product[0]} | name : {product[1]} | purchase price : {product[2]} | sell price : {product[3]} | crunt stock : {product[4]}\n")