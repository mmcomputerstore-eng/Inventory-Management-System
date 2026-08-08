from database import connect_database
from search_product import Search
@connect_database
def counform_delete(self,products):
    while True:
        try:
            counform = int(input(f"Please Eanter 1 to Delete Product eater 0 to exit : "))
            if counform == 1:
                self.cursor.execute("delete from products where ID = %s",(products[0][0],))
                print(f"Product ID {products[0][0]} Deleted Successfully...")
                break
            elif counform == 0:
                break
            else:
                print("You Have Only 2 Option (1) or (0) Please Eanter 1 of Them...")
        except ValueError:
            print("You Have Only 2 Option (1) or (0) Please Eanter 1 of Them...")
def delete_product(self):
    products = Search(self,"Delete")
    counform_delete(self,products)
