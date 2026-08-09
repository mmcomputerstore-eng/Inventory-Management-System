from database import connect_database
from supplier_management import show_supplier
from datetime import date

@connect_database
def purchase(self):
    while True:
        try:
            supplier_id = int(input( "Eanter Supplier ID : "))
            self.cursor.execute("Select ID,Name,Email,Phone from suppliers where ID = %s",(supplier_id,))
            supplier = self.cursor.fetchone()
            if supplier == None:
                print(f"No Supplier Found With ID {supplier_id} Please Eanter a Valid Supplier ID...")
            else:
                show_supplier(supplier)
                print ("Supplier is Selected for This pruchase...")
                break
        except ValueError:
            print("Supplier ID Must in Numbers like 123...\nTry Again")
    purchase_products =()
    while True:
        if len(purchase_products) >=1:
            print("=== if You not want to Add more Products Hit Eanter ===")
        product_id_name = input("Eanter Product ID or Name : ")
        if product_id_name == "" and len(purchase_products) >=1:
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
                        purchase_price = input(f"Eanter Purchase Price or Hit Eanter to Contineu With {product[2]} : ")
                        if purchase_price == "":
                            purchase_price = product[2]
                            break
                        else:
                            purchase_price = int(purchase_price)
                            break
                    except ValueError:
                        print("Please Eanter purchase Price in numbers like 123...")
                while True:
                    try:
                        purchase_units = int(input("Eanter Quantity : "))
                        if purchase_units >=1:
                            break
                        else:
                            print(f"Quantity Must be 1 or more then 1 Not {purchase_units}\n Try Again")
                        
                    except ValueError:
                        print("Please Eanter Quantity in numbers like 123...")
                purchase_products += ([product[0],purchase_price,purchase_units],)
    if len(purchase_products) >=1:
        purchase_date = date.today().isoformat()
        total = sum(product[1]*product[2] for product in purchase_products)
        self.cursor.execute("insert into purchases(supplier_id,date,Total) values (%s,%s,%s)",(supplier_id,purchase_date,total))
        self.cursor.execute("SELECT id,supplier_id,date,Total FROM purchases ORDER BY id DESC LIMIT 1")
        purchase = self.cursor.fetchone()
        print(f"=== Purchase Details ===\nPurchase ID : {purchase[0]} | Supplier_id : {purchase[1]} | Date : {purchase[2]} | Total : {purchase[3]}")
        for product in purchase_products:
            self.cursor.execute("update products set Crunt_stock = Crunt_stock+%s where ID = %s",(product[2],product[0]))
            self.cursor.execute("insert into purchases_details(purchase_id,product_id,quantity,price) values(%s,%s,%s,%s)",(purchase[0],product[0],product[2],product[1]))
            print(f"Product ID : {product[0]} | Quantity : {product[2]} | Price : {product[1]}")
    print("Purchase Compleated...")