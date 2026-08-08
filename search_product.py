from database import connect_database
@connect_database
def Search(self):
    search =input("Please Eanter Product Name or ID to Search : ")
    self.cursor.execute("select ID,Product_name,Purchase_Price,Crunt_stock from products where ID = %s or product_name = %s",(search,search))
    products = self.cursor.fetchall()
    if products == None:
        print (f"No Product Found With Name or ID : {search}")
    else:
        for product in products:
            print(f"=== Product Details ===\nProduct ID : {product[0]} | Product Name : {product[1]} | Product Price : {product[2]} | Stock : {product[3]}")
    
