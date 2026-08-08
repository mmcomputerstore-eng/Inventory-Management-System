from database import connect_database
@connect_database
def Search(self,opration):
    search =input(f"Please Eanter Product Name or ID to {opration} : ")
    self.cursor.execute("select ID,Product_name,Purchase_Price,Crunt_stock,Sell_Price from products where ID = %s or product_name = %s",(search,search))
    products = self.cursor.fetchall()
    if products == None:
        print (f"No Product Found With Name or ID : {search}")
    else:
        for product in products:
            print(f"=== Product Details ===\nProduct ID : {product[0]} | Product Name : {product[1]} | Purchase Price : {product[2]} | Sell Price : {product[4]} | Stock : {product[3]} ")
        if opration == "Update":
            return products