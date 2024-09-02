import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


if __name__ == '__main__':
    
    print("--------> welcome to the farmers connections <--------")

    while(True):
        print("\n\nMenu")
        print("1.Register (for new users only)")
        print("2.Login (for existing users only)")
        print("3.Exit")

        ch=int(input("Enter your choice: "))

        if ch==1:
            continue
        elif ch==2:
            print("Login")
        elif ch==3:
            print("Thank you for using our application")
            break


