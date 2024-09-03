import re

import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def verify_the_email() -> bool:
    pass

def verify_the_user_login() -> bool:
    pass

def verify_via_otp() -> bool:
    pass

def create_new_farmer_user() :
    verify_via_otp()
    cursor.execute("INSERT INTO farmer VALUES (?,?,?,?)", (name, email, phone, password))
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



