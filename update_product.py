from database import connect_database
from search_product import Search
def get_int(value_name, old_value):
    while True:
        try:
            value = input(
                f"Enter New {value_name} or hit Enter to continue with {old_value}: "
            )

            if value == "":
                return old_value

            return int(value)

        except ValueError:
            print(f"Please Enter {value_name} in numbers like 123...")

@connect_database
def update_product(self,products):
    if products is not None:
            new_name = input(f"Eanter New Product Name or Hit Eanter to Countinu with {products[0][1]} : ")
            new_price = get_int("Selling Price",products[0][4])
            new_stock = get_int("Stock",products[0][3])
            if new_name != products[0][1] or new_price != products[0][4] or new_stock != products[0][3]:
                self.cursor.execute("update products set Product_name = %s , Sell_Price = %s ,Crunt_stock = %s where ID = %s",(new_name,new_price,new_stock,products[0][0]))
                print ("Product Updated Successfully...")
            else:
                print("You are Not Updating Any Thing...")

def update(self):
    products = Search(self,"Update")
    update_product(self,products)
        