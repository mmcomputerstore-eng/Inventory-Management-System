class Menu:
    def __init__(self):
        while True:
            print("=== Menu ===\n1. Add Product")
            try:
                a = int(input("Enter option Number to contineu : "))
            except ValueError:
                print("Please Eanter option Number like 1 for Add Product ...")