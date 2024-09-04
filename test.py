import sqlite3

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
    conn = sqlite3.connect('database.db')
    with conn:
        conn.execute(CREATE_FARMERS)
        print("ok")

create_farmers_table()

# SQL Commands
CREATE_PRODUCT_PAGE = '''
CREATE TABLE IF NOT EXISTS product_page (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    capacity TEXT,
    price REAL,
    available_product BOOLEAN,
    duration TEXT
);
'''
def create_product_page_table():
    conn = sqlite3.connect('products.db')
    with conn:
        conn.execute(CREATE_PRODUCT_PAGE)
        print("ok")
create_product_page_table()
