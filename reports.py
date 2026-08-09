from database import connect_database
def reports_menu(self):
    while True:
        try:
            print("== Reports ==\n1. Low Stock\n2. Exit to Main Menu")
            option = int(input("Eanter Option Number to contineu : "))
            if option == 1:
                low_stock(self)
            elif option == 2:
                print("Exit Successfull...")
                break
            else:
                print ("invalid Option Number..\nPlease Eanter a Valid Option Number Try Again...")
        except ValueError:
            print("Please eanter Option Number Like (1) for Low Stock...")

@connect_database
def low_stock(self):
    self.cursor.execute("select id ,product_name,Crunt_stock from products Where Crunt_stock < 5")
    products = self.cursor.fetchall()
    if len(products) == 0:
        print("No Product Found With low Stock..")
    else:
        print("=== Low Stock Products ===")
        for product in products:
            print(f"Product ID : {product[0]} | Product Name : {product[1]} | Crunt Stock : {product[2]}")