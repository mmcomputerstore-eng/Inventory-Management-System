from database import connect_database

@connect_database
def View_products(self):
    self.cursor.execute("select ID,Product_name,Purchase_Price,Crunt_stock from products")
    data = self.cursor.fetchall()
    if not data:
        print('No Product Found in Record...')
    else:
        print("=== Products ===")
        for product in data:
            print(f"Product ID : {product[0]} | Name : {product[1]} | Price : {product[2]} | Stock : {product[3]}")
        print()
