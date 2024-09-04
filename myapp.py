from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import re
import sqlite3
import random
from twilio.rest import Client

# Database connection
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def is_valid_phone_number(phone_number: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone_number) is not None

def buy_products():
    pass

def pre_booking():
    pass

def add_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def display_all_products():
    pass

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

class RegisterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text="Confirm Password:"))
        self.c_password = TextInput(password=True, multiline=False)
        self.add_widget(self.c_password)

        self.add_widget(Label(text="Phone Number:"))
        self.phone_number = TextInput(multiline=False)
        self.add_widget(self.phone_number)

        self.register_button = Button(text="Register", on_press=self.register_user)
        self.add_widget(self.register_button)

    def register_user(self, instance):
        email = self.email.text
        password = self.password.text
        c_password = self.c_password.text
        phone_number = self.phone_number.text

        if not verify_the_email(email):
            self.show_popup("Invalid email format.")
            return

        if password != c_password:
            self.show_popup("Passwords do not match.")
            return

        if not is_valid_phone_number(phone_number):
            self.show_popup("Invalid phone number.")
            return

        if verify_via_otp(phone_number):
            cursor.execute("INSERT INTO consumers (email, password, phonenumber) VALUES (?, ?, ?)",
                           (email, password, phone_number))
            connection.commit()
            self.show_popup("Registration successful.")
        else:
            self.show_popup("OTP verification failed.")

    def show_popup(self, message):
        popup = Popup(title='Notification',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_button = Button(text="Login", on_press=self.login_user)
        self.add_widget(self.login_button)

    def login_user(self, instance):
        email = self.email.text
        password = self.password.text

        if verify_the_email(email):
            cursor.execute("SELECT * FROM consumers WHERE email=? AND password=?", (email, password))
            user = cursor.fetchone()
            if user:
                self.show_popup("Login successful.")
                # Proceed to next screen or functionality
            else:
                self.show_popup("Invalid email or password.")
        else:
            self.show_popup("Invalid email format.")

    def show_popup(self, message):
        popup = Popup(title='Notification',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class MyApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')

        self.register_button = Button(text="Register", on_press=self.show_register_screen)
        self.main_layout.add_widget(self.register_button)

        self.login_button = Button(text="Login", on_press=self.show_login_screen)
        self.main_layout.add_widget(self.login_button)

        return self.main_layout

    def show_register_screen(self, instance):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(RegisterScreen())

    def show_login_screen(self, instance):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(LoginScreen())

if __name__ == "__main__":
    MyApp().run()
