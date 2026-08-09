from database import connect_database
import re


def customers_menu(self):
    while True:
        print("=== Customer Management ===\n1. Add Customer\n2. View Customer\n3. Exit to Main Menu")

        try:
            option = int(input("Enter Option Number to Select : "))

            if option == 1:
                add_customer(self)

            elif option == 2:
                view_customer(self)

            elif option == 3:
                print("Exit Successfully...")
                break

            else:
                print("Please Enter Option Number (1) for Add Customer (2) for View Customers...")

        except Exception as e:
            print(e)
            print("Please Enter Option Number (1) for Add Customer (2) for View Customers...")


def show_customer(customer):
    print(
        f"Customer ID : {customer[0]} | "
        f"Customer Name : {customer[1]} | "
        f"Customer Email : {customer[2]} | "
        f"Customer Phone : {customer[3]}"
    )


@connect_database
def view_customer(self):
    self.cursor.execute(
        "SELECT ID, Name, Email, Phone FROM customers"
    )

    customers = self.cursor.fetchall()

    if len(customers) == 0:
        print("No Customer Found..")

    else:
        for customer in customers:
            show_customer(customer)



@connect_database
def add_customer(self):
    new_name = input("Enter Customer Name : ")

    # Check duplicate customer name
    self.cursor.execute(
        "SELECT ID, Name, Email, Phone FROM customers WHERE Name = %s",
        (new_name,)
    )

    check_duplicate = self.cursor.fetchone()

    if check_duplicate is None:

        # Email validation
        while True:
            new_email = input("Enter Email Address : ")

            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.fullmatch(pattern, new_email):

                # Check duplicate email
                self.cursor.execute(
                    "SELECT ID, Name, Email, Phone FROM customers WHERE Email = %s",
                    (new_email,)
                )

                check_duplicate_email = self.cursor.fetchone()

                if check_duplicate_email is None:
                    break

                else:
                    print(
                        f"Email {new_email} Already Found. "
                        "Duplicate Email Not Allowed..."
                    )
                    show_customer(check_duplicate_email)

            else:
                print("Invalid Email...")

        new_phone = input("Enter Customer Phone Number : ")

        # Insert customer
        self.cursor.execute(
            "INSERT INTO customers(Name, Email, Phone) VALUES(%s, %s, %s)",
            (new_name, new_email, new_phone)
        )

        print(f"New Customer Name {new_name} Added Successfully...")

    else:
        print(
            f"Customer Name {new_name} Already Found in Record. "
            "Duplicate Name Not Allowed..."
        )

        show_customer(check_duplicate)