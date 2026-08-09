from database import connect_database
from view_products import View_products
from search_product import Search
from update_product import update
from delete_product import delete_product
from product_category_management import menu
from supplier_management import suppliers_menu
from purchase import purchase
class Menu:
    def run(self):
        self.product= ProductManager()
        while True:
            print("=== Menu ===\n1. Add Product\n2. View All Products\n3. Search Products\n4. Update Product\n5. Delete Product\n6. Catagory Management\n7. Supplier Management\n8. Purchase\n9. Exit")
            try:
                choice = int(input("Enter option Number to contineu : "))
                if choice == 1:
                    self.product.add_products()
                elif choice == 2:
                    View_products(self)
                elif choice == 3:
                    Search(self,"Search")
                elif choice == 4:
                    update(self)
                elif choice == 5:
                    delete_product(self)
                elif choice == 6:
                    menu(self)
                elif choice == 7:
                    suppliers_menu(self)
                elif choice ==8:
                    purchase(self)
                elif choice == 9:
                    print("Exit Successfull...")
                    break
            except ValueError:
                print("Please Eanter option Number like 1 for Add Product ...")
class ProductManager:
    @connect_database
    def add_product(self):
        name = input("Eanter Product Name : ")
        self.cursor.execute("select * from products where product_name = %s",(name,))
        product = self.cursor.fetchone()
        if product ==None:
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

m = Menu()
m.run()