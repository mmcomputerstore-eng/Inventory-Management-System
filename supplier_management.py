from database import connect_database
def suppliers_menu(self):
    while True:
        print("=== Supplier Management ===\n1. Add Supplier\n2. View Supplier\n3. Exit to Main Menu")
        try:
            option = int(input("Eanter Option Number to Select : "))
            if option == 1 :
                add_supplier(self)
            elif option == 2:
                view_supplier(self)
            elif option == 3:
                print("Exit Successfull...")
                break
            else:
                print("Please Eanter Write Option Number (1) for Add Catagory (2) for View Catagorys...")
        except Exception as e:
            print(e)
            print("Please Eanter Option Number (1) for Add Catagory (2) for View Catagorys...")
@connect_database
def view_supplier(self):
    self.cursor.execute("Select ID,Name,Email,Phone from suppliers")
    suppliers = self.cursor.fetchall()
    if len(suppliers) == 0:
        print("No Supplier Found..")
    else:
        for supplier in suppliers:
            print(f"Supplier ID : {supplier[0]} | Supplier Name : {supplier[1]} | Supplier Email : {supplier[2]} | Supplier Phone : {supplier[3]}")