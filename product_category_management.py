from database import connect_database
def menu(self):
    while True:
        print("=== Catagory Management ===\n1. Add Catagory\n2. View Catagorys\n3. Exit to Main Menu")
        try:
            option = int(input("Eanter Option Number to Select : "))
            if option == 1 :
                add_catagory(self)
            elif option == 2:
                view_catagory(self)
            elif option == 3:
                print("Exit Successfull...")
                break
            else:
                print("Please Eanter Write Option Number (1) for Add Catagory (2) for View Catagorys...")
        except Exception as e:
            print(e)
            print("Please Eanter Option Number (1) for Add Catagory (2) for View Catagorys...")

@connect_database
def view_catagory(self):
    self.cursor.execute("Select ID,Category_name from product_category")
    catagorys = self.cursor.fetchall()
    if len(catagorys) == 0:
        print("No Catagory Found..")
    else:
        for catagory in catagorys:
            print(f"Catagory ID : {catagory[0]} | Catagory Name : {catagory[1]}")

@connect_database
def add_catagory(self):
    catagory_name = input("Eanter catagory Name : ")
    self.cursor.execute("Select ID,Category_name from product_category where Category_name = %s",(catagory_name,))
    old_same_catagory = self.cursor.fetchone()
    if old_same_catagory == None:
        self.cursor.execute("insert into product_category (Category_name) values(%s)",(catagory_name,))
        self.cursor.execute("Select ID,Category_name from product_category where Category_name = %s",(catagory_name,))
        new_catagory = self.cursor.fetchone()
        print(f"New Catagory Added Successfully | Name : {new_catagory[1]} | ID : {new_catagory[0]}")
    else:
        print(f"Catagory Name {catagory_name} Already found in Record with Catagory ID {old_same_catagory[0]} Dublaicate Catagory Not Allow...")