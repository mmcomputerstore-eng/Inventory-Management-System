from database import connect_database
from datetime import date
from coustomers import show_customer
@connect_database
def sales(self):
    while True:
        try:
            coustomer_id = int(input( "Eanter Supplier ID : "))
            self.cursor.execute("SELECT ID, Name, Email, Phone FROM customers Where ID = %s",(coustomer_id,))
            coustomer = self.cursor.fetchone()
            if coustomer == None:
                print(f"No Coustomer Found With ID {coustomer_id} Please Eanter a Valid Coustomer ID...")
            else:
                show_customer(coustomer)
                print ("Coustomer is Selected for This pruchase...")
                break
        except ValueError:
            print("Coustomer ID Must in Numbers like 123...\nTry Again")
    sell_products =()
    while True:
        if len(sell_products) >=1:
            print("=== if You not want to Add more Products Hit Eanter ===")
        product_id_name = input("Eanter Product ID or Name : ")
        if product_id_name == "" and len(sell_products) >=1:
            break
        else:   
            self.cursor.execute("select ID,Product_name,Purchase_Price,Crunt_stock,Sell_Price from products where ID = %s or product_name = %s",(product_id_name,product_id_name))
            product = self.cursor.fetchone()
            if product == None:
                print(f"No Product found with Name or ID {product_id_name}\n Try Again")
            else:
                print(f"Product ID : {product[0]} | Product Name : {product[1]} | Purchase Price : {product[2]} |Sell Price : {product[4]} | Crunt Stock : {product[3]} ")
                while True:
                    try:
                        Selling_price = input(f"Eanter Selling Price or Hit Eanter to Contineu With {product[4]} : ")
                        if Selling_price == "":
                            Selling_price = product[4]
                            break
                        else:
                            Selling_price = int(Selling_price)
                            break
                    except ValueError:
                        print("Please Eanter Selling Price in numbers like 123...")
                while True:
                    try:
                        Selling_units = int(input("Eanter Quantity : "))
                        if Selling_units >=1:
                            break
                        else:
                            print(f"Quantity Must be 1 or more then 1 Not {Selling_units}\n Try Again")
                        
                    except ValueError:
                        print("Please Eanter Quantity in numbers like 123...")
                sell_products += ([product[0],Selling_price,Selling_units],)
    if len(sell_products) >=1:
        sell_date = date.today().isoformat()
        total = sum(product[1]*product[2] for product in sell_products)
        self.cursor.execute("insert into sales(customer_id,date,Total) values (%s,%s,%s)",(coustomer_id,sell_date,total))
        self.cursor.execute("SELECT id,customer_id,date,Total FROM purchases ORDER BY id DESC LIMIT 1")
        sale = self.cursor.fetchone()
        print(f"=== Sale Details ===\nSale ID : {sale[0]} | Coustomer ID : {sale[1]} | Date : {sale[2]} | Total : {sale[3]}")
        for product in sell_products:
            self.cursor.execute("update products set Crunt_stock = Crunt_stock+%s where ID = %s",(product[2],product[0]))
            self.cursor.execute("insert into purchases_details(purchase_id,product_id,quantity,price) values(%s,%s,%s,%s)",(sale[0],product[0],product[2],product[1]))
            print(f"Product ID : {product[0]} | Quantity : {product[2]} | Price : {product[1]}")
    print("Sale Compleated...")