import sqlite3
connection = sqlite3.connect('.db')
cursor = connection.cursor()

def buy_products(product_name, product_capacity, delivery_date):

    product_name = input("Enter the product name: ")
    product_capacity = input("Enter the product capacity: ")
    delivery_date = input("Enter the delivery date (YYYY-MM-DD): ")

    INSERT_PRODUCT = '''
    INSERT INTO Products (ProductName, ProductCapacity, DeliveryDate)
    VALUES (?, ?, ?);
    '''

    cursor.execute(INSERT_PRODUCT, (product_name, product_capacity, delivery_date))
    connection.commit()
    connection.close()

    print(f"Purchase confirmed for {product_name} with a capacity of {product_capacity}. Delivery is scheduled for {delivery_date}.")

buy_products()
import sqlite3

# Establishing a connection to the database
connection = sqlite3.connect('farmer_requests.db')
cursor = connection.cursor()

# Function to pre-book a product
def pre_booking():
    # Prompt user for input
    product_name = input("Enter the product name for pre-booking: ")
    product_capacity = input("Enter the product capacity: ")
    delivery_date = input("Enter the delivery date (YYYY-MM-DD): ")

    # SQL command to insert a new record into the Products table
    INSERT_PRODUCT = '''
    INSERT INTO Products (ProductName, ProductCapacity, DeliveryDate)
    VALUES (?, ?, ?);
    '''

    # Execute the command and commit the changes
    cursor.execute(INSERT_PRODUCT, (product_name, product_capacity, delivery_date))
    connection.commit()

    # Display a confirmation message
    print(f"Pre-booking confirmed for {product_name} with a capacity of {product_capacity}. Delivery is scheduled for {delivery_date}.")

# Example usage of pre_booking function
pre_booking()

connection.close()

import sqlite3

# SQL Commands
CREATE_PRODUCTS = '''
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Description TEXT,
    ProductCapacity TEXT,
    ProductPrice REAL,
    ProductAvailability BOOLEAN,
    ProductDuration TEXT
);
'''

INSERT_PRODUCT = '''
INSERT INTO Products (ProductName, Description, ProductCapacity, ProductPrice, ProductAvailability, ProductDuration)
VALUES (?, ?, ?, ?, ?, ?);
'''

SELECT_ALL_PRODUCTS = '''
SELECT * FROM Products;
'''

SELECT_PRODUCT_BY_NAME = '''
SELECT * FROM Products WHERE ProductName = ?;
'''

DELETE_PRODUCT = '''
DELETE FROM Products WHERE ProductName = ?;
'''

# Function to create the Products table
def create_products_table():
    conn = sqlite3.connect('products.db')
    with conn:
        conn.execute(CREATE_PRODUCTS)
    conn.close()

# Function to insert a product into the Products table
def add_products(product_name, description, product_capacity, product_price, product_availability, product_duration):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_PRODUCT, (product_name, description, product_capacity, product_price, product_availability, product_duration))
        conn.commit()
    conn.close()

    print(f"Product '{product_name}' added successfully with a capacity of '{product_capacity}', priced at {product_price}. Availability: {product_availability}. Duration: {product_duration}.")

# Function to select all products
def select_all_products():
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_PRODUCTS)
        products = c.fetchall()
        output = ''
        for product in products:
            output += (f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, "
                       f"Capacity: {product[3]}, Price: {product[4]}, "
                       f"Available: {product[5]}, Duration: {product[6]}\n")
    conn.close()
    return output

# Function to select a specific product by name
def select_product_by_name(product_name):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_PRODUCT_BY_NAME, (product_name,))
        product = c.fetchone()
        output = ''
        if product:
            output = (f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, "
                      f"Capacity: {product[3]}, Price: {product[4]}, "
                      f"Available: {product[5]}, Duration: {product[6]}")
    conn.close()
    return output

# Function to delete a product by name
def delete_product(product_name):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_PRODUCT, (product_name,))
        conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_products_table()  # Create the table if it doesn't exist

    # Take user inputs
    product_name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    product_capacity = input("Enter the product capacity: ")
    product_price = float(input("Enter the product price: "))
    product_availability = input("Is the product available (True/False)? ").lower() in ['true', 'yes', '1']
    product_duration = input("Enter the product duration: ")

    # Add the product
    add_products(product_name, description, product_capacity, product_price, product_availability, product_duration)

    # Display all products
    print("\nAll Products:")
    print(select_all_products())

    # Select and print a specific product
    print("\nProduct Details:")
    print(select_product_by_name(product_name))
    
    # Optionally delete a product
    delete = input("\nDo you want to delete this product? (yes/no): ").strip().lower()
    if delete == 'yes':
        delete_product(product_name)
        print("\nProduct deleted.")
        print("\nAll Products after deletion:")
        print(select_all_products())
