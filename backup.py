import re

from twilio.rest import Client
import random

import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def is_valid_phone_number(phone_number: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone_number) is not None

def display_all_products():
    cursor.execute("SELECT * FROM product_page")
    products = cursor.fetchall()
    for product in products:
        print(product)

def buy_products():

    product = input("Enter the product name: ")
    capacity = input("Enter the product capacity: ")
    date = input("Enter the delivery date (YYYY-MM-DD): ")

    INSERT_PRODUCT = '''
    INSERT INTO request_farmers (product, capacity, date)
    VALUES (?, ?, ?);
    '''
    # cursor.execute("insert into consumers (buyed_products) values (?)", (product_name,))

    
    cursor.execute(INSERT_PRODUCT, (product, capacity, date))

    connection.commit()

    print(f"Purchase confirmed for {product} with a capacity of {capacity}. Delivery is scheduled for {date}.")


def pre_booking():
    # Prompt user for input
    name = input("Enter the product name for pre-booking: ")
    capacity = input("Enter the product capacity: ")
    date = input("Enter the delivery date (YYYY-MM-DD): ")

    # SQL command to insert a new record into the Products table
    INSERT_PRODUCT = '''
    INSERT INTO request_farmers_prebooking (product, capacity, date)
    VALUES (?, ?, ?);
    '''
    # cursor.execute("insert into consumers (prebooked_products) values (?)", (product_name,))

    # Execute the command and commit the changes
    cursor.execute(INSERT_PRODUCT, (name, capacity, date))
    connection.commit()

    # Display a confirmation message
    print(f"Pre-booking confirmed for {name} with a capacity of {capacity}. Delivery is scheduled for {date}.")

def add_product():

    product_name = input("Enter the product name: ")
    product_description = input("Enter the description: ")
    product_capacity = input("Enter the product capacity: ")
    product_price = input("Enter the product price: ")
    product_avaliability = "yes" if input("Is the product available? (yes/no): ") == "yes" else "no"
    duration = input("enter the duration:")

    INSERT_PRODUCT = '''
    INSERT INTO product_page (name, description, capacity,price,available_product,duration)
    VALUES (?, ?, ?, ?, ?, ?);
    '''
    
    cursor.execute(INSERT_PRODUCT, (product_name, product_description, product_capacity, product_price, product_avaliability, duration))

    connection.commit()

    print("\nproduct added successfully")

def update_product():
    display_all_products()
    product_name = input("Enter the product name: ")
    field_name =  input("Enter the field name: ")
    new_value = input("Enter the new value to insert: ")

    query = f"UPDATE product_page SET {field_name} = ? WHERE name = ?"
    
    # Execute the update query
    cursor.execute(query, (new_value, product_name))
    connection.commit()

    print(f"Product ID {product_name} updated successfully!")

def delete_product():
    display_all_products()
    product_name = input("Enter the product name to delete: ")
    cursor.execute("delete from product_page where name = ?", (product_name,))
    connection.commit()


def verify_the_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def verify_the_user_login() -> tuple[ bool, str]:

    user_type = input("Enter 'farmer' or 'consumer': ")
    table_name = 'farmers' if user_type == 'farmer' else 'consumers'

    while(True):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if verify_the_email(email):

            cursor.execute(f"SELECT * FROM {table_name} WHERE email=? AND password=?", (email, password))
            user = cursor.fetchone()
            if user:
                print(f"\nWelcome back, {email}!")
                return True,user_type
            else:
                print("\nInvalid username or password.")
                return False , user_type
        
        else:
            print("\nInvalid email format. Please enter a valid email.")



def verify_via_otp(to_phone_number: str) -> bool:

    """
    This function sends a message to the given phone number with a random OTP and prompts the user to enter the OTP.
    If the OTP entered by the user matches the sent OTP, then the function returns True, else False.
    This function is to be used for verification of the user's phone number.
    
    Parameters:
    to_phone_number (str): The phone number to which the OTP message is to be sent.
    
    Returns:
    bool: True if the OTP entered by the user matches the sent OTP else False.
    
    """

    account_sid = 'ACa7fc0ab9bb23712402dff867549c01e8'
    auth_token = 'eda3e6f494371539e101a59ba7f0e4b8'

    otp = str(random.randint(100000, 999999))
    message = Client(account_sid, auth_token).messages.create(
        body=f"Your OTP is {otp}",
        from_='+18307420985',
        to= '+91' + to_phone_number
    )

    if(otp == input("Enter OTP: ")):
        return True
    else:
        return False

def create_new_farmer_user() :
    print("---- Farmer  Registration ----")
    
    email = ''
    address = ''
    password = ''
    c_password = ''
    phone_number = ''
    pincode  = ''
    products = ''

    while(True):
        email = input("Enter your email: ")
        if verify_the_email(email):
            break
        else:
            print("\nInvalid email. Please try again.")



    address = input("Enter your address: ")

    while(True):
        password = input("Enter your password: ")
        c_password = input("Confirm your password: ")
        if password == c_password:
            break
        else:
            print("Passwords don't match. Please try again.")

    while(True):
        phone_number = input("Enter your phone number: ")
        if is_valid_phone_number(phone_number):
            break
        else:
            print("\nInvalid phone number. Please try again.")

    pincode = input("Enter your pincode: ")

    products = input("(please separate the products by comma)Enter your products: ")

    if verify_via_otp(phone_number):
        cursor.execute("INSERT INTO farmers (email, address, password, phone_number, pincode, products) VALUES (?, ?, ?, ?, ?, ?)",
                       (email, address, password,phone_number,  pincode, products))
        connection.commit()
        print("\n Farmer user created successfully.\n")
    else:
        print("Failed to create farmer user.")
        return None

def create_new_consumer_user():
    print("---- Consumer Registration ----")
    
    email = ''
    password = ''
    c_password = ''
    phone_number = ''

    while(True):
        email = input("Enter your email: ")
        if verify_the_email(email):
            break
        else:
            print("\nInvalid email. Please try again.")



    while(True):
        password = input("Enter your password: ")
        c_password = input("Confirm your password: ")
        if password == c_password:
            break
        else:
            print("Passwords don't match. Please try again.")

    while(True):
        phone_number = input("Enter your phone number: ")
        if is_valid_phone_number(phone_number):
            break
        else:
            print("\nInvalid phone number. Please try again.")


    if verify_via_otp(phone_number):
        cursor.execute("INSERT INTO consumers (email, password, phonenumber) VALUES (?, ?, ?)",
                       (email, password, phone_number))
        connection.commit()
        print("\nConsumer user created successfully.\n")
    else:
        print("Failed to create consumer user.")
        return None

if __name__ == '__main__':
    
    print("--------> welcome to the farmers connections <--------")

    while(True):

        print("\n\n---- Menu ----\n")
        print("1.Register (for new users only)")
        print("2.Login (for existing users only)")
        print("3.Exit")

        ch=int(input("\nEnter your choice: "))

        if ch==1:

            while(True):

                print("\n1. farmer")
                print("2. consumer")
                print("3. Exit\n")

                ch=int(input("\nEnter your choice: "))

                if ch==1:
                    create_new_farmer_user()
                    break
                elif ch==2:
                    create_new_consumer_user()
                    break
                elif ch==3:
                    print("\ngetting back to menu")
                    break

        elif ch==2:

            flag , user = verify_the_user_login()
            if flag:

                print("\nlogin successful")
                print("\n---- Home ----\n")

                if(user == "farmer"):

                    while(True):
                        print("---- menu ----")
                        print("\n1. Add product")
                        print("2. Update product")
                        print("3. Delete product")
                        print("4. view the aviable products")
                        print("5. Exit\n")

                        ch=int(input("\nEnter your choice: "))

                        if ch==1:
                            add_product()
                        elif ch==2:
                            update_product()
                        elif ch==3:
                            delete_product()
                        elif ch==4:
                            display_all_products()
                        elif ch==5:
                            print("\ngetting back to menu")
                            break

                elif(user == "consumer"):

                    print("\n---- menu ----")

                    display_all_products()
                    while(True):
                        print("1. buy products")
                        print("2. pre booking ")
                        print("3. Exit\n")

                        ch=int(input("\nEnter your choice: "))

                        if ch==1:
                            buy_products()
                        elif ch==2:
                            pre_booking()
                        elif ch==3:
                            print("\ngetting back to menu")
                            break


            else:

                print("\nlogin failed")

        elif ch==3:

            print("\nThank you for using our application")
            break



