from database import connect_database
import re
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
def show_supplier(supplier):
    print(f"Supplier ID : {supplier[0]} | Supplier Name : {supplier[1]} | Supplier Email : {supplier[2]} | Supplier Phone : {supplier[3]}")

@connect_database
def view_supplier(self):
    self.cursor.execute("Select ID,Name,Email,Phone from suppliers")
    suppliers = self.cursor.fetchall()
    if len(suppliers) == 0:
        print("No Supplier Found..")
    else:
        for supplier in suppliers:
            show_supplier(supplier)
@connect_database
def add_supplier(self):
    new_name = input("Eanter supplier Name : ")
    self.cursor.execute("Select ID,Name,Email,Phone from suppliers where name = %s",(new_name,))
    check_dublicate = self.cursor.fetchone()
    if check_dublicate == None:
        while True:
                new_email = input("Eanter Eamil Address : ")
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if re.fullmatch(pattern, new_email):
                    self.cursor.execute("Select ID,Name,Email,Phone from suppliers where Email = %s",(new_email,))
                    check_dublicate_email = self.cursor.fetchone()
                    if check_dublicate_email == None:
                        break
                    else:
                        print(f"Eamil {new_email} Allready found Dublicate Eamil Not Allowd...")
                        show_supplier(check_dublicate_email)
                    
                else:
                    print("invalid Eamil...")
        new_phone = input("Eanter supplier Phone Number : ")
        self.cursor.execute("insert into suppliers(Name,Email,Phone) values(%s,%s,%s)",(new_name,new_email,new_phone))
        print(f"New supplier Name {new_name} Added Successfully...")
    else:
        print(f"Supplier name {new_name} Allredy found in Record Dublicate Name Not Allowd...")
        show_supplier(check_dublicate)

