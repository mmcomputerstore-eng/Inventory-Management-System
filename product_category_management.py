def menu(self):
    while True:
        print("=== Catagory Management ===\n1. Add Catagory\n2. View Catagorys\n3. Delete Catagory\n4. Exit to Main Menu")
        try:
            option = int(input("Eanter Option Number to Select : "))
            if option == 1 :
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                print("Exit Successfull...")
                break
            else:
                print("Please Eanter Write Option Number (1) for Add Catagory (2) for View Catagorys...")
        except:
            print("Please Eanter Option Number (1) for Add Catagory (2) for View Catagorys...")

