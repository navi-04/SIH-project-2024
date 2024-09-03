import re

from twilio.rest import Client
import random

import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def verify_the_email() -> bool:
    pass

def verify_the_user_login() -> bool:
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

    account_sid = 'AC43a68689f9067780b21993d830e39c8f'
    auth_token = '7795b97e29dc833c8bb6416c132c30b8'
    otp = str(random.randint(100000, 999999))
    message = Client(account_sid, auth_token).messages.create(
        body=f"Your OTP is {otp}",
        from_='+18315083621',
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
        print("\n\nMenu")
        print("1.Register (for new users only)")
        print("2.Login (for existing users only)")
        print("3.Exit")

        ch=int(input("Enter your choice: "))

        if ch==1:
            while(True):
                print("1. farmer")
                print("2. consumer")
                print("3. Exit")
                ch=int(input("Enter your choice: "))
                if ch==1:
                    create_new_farmer_user()
                elif ch==2:
                    create_new_consumer_user()
                elif ch==3:
                    print("getting back to menu")
                    break
        elif ch==2:
            verify_the_user_login()
        elif ch==3:
            print("Thank you for using our application")
            break



