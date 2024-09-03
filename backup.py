import re

from twilio.rest import Client
import random

import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def add_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def display_all_products():
    pass

def is_valid_email(email: str) -> bool:

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def verify_the_email(email: str) -> bool:
    if is_valid_email(email):
        return True
    else:
        print("Invalid email format. Please enter a valid email.")
        return False
    pass

def verify_the_user_login() -> tuple[ bool, str]:
    pass

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
        to=to_phone_number
    )

    if(otp == input("Enter OTP: ")):
        return True
    else:
        return False

def create_new_farmer_user() :
    verify_via_otp()
    pass

def create_new_consumer_user():
    print("user")
    pass

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
                elif ch==2:
                    create_new_consumer_user()
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
                    pass

            else:

                print("\nlogin failed")

        elif ch==3:

            print("\nThank you for using our application")
            break



