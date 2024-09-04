import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# SQL commands to create the table
CREATE_FARMERS = '''
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    password VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    products TEXT
);
'''

def create_farmers_table():
        cursor.execute(CREATE_FARMERS)
        print("ok")

print(cursor.execute("SELECT * FROM farmers").fetchall())




