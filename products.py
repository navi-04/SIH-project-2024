import sqlite3

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

INSERT_PRODUCT_PAGE = '''
INSERT INTO product_page (name, description, capacity, price, available_product, duration)
VALUES (?, ?, ?, ?, ?, ?);
'''

SELECT_ALL_PRODUCTS = '''
SELECT * FROM product_page;
'''

SELECT_PRODUCT_BY_NAME_AND_PRICE = '''
SELECT * FROM product_page WHERE name = ? AND price = ?;
'''

DELETE_PRODUCT = '''
DELETE FROM product_page WHERE name = ? AND price = ?;
'''

# Function to create the product_page table
def create_product_page_table():
    conn = sqlite3.connect('products.db')
    with conn:
        conn.execute(CREATE_PRODUCT_PAGE)

# Function to insert a product into the product_page table
def insert_product(name, description, capacity, price, available_product, duration):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_PRODUCT_PAGE, (name, description, capacity, price, available_product, duration))
        conn.commit()

# Function to select all products
def select_all_products():
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_PRODUCTS)
        # Store data into a list of tuples
        products = c.fetchall()
        c.close()
        output = ''
        for product in products:
            output += f"{product[1]} {product[2]} {product[3]} {product[4]} {product[5]} {product[6]}\n"
        return output

# Function to select a specific product by name and price
def select_product_by_name_and_price(name, price):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_PRODUCT_BY_NAME_AND_PRICE, (name, price))
        # Store data into a list of tuples
        products = c.fetchall()
        c.close()
        output = ''
        for product in products:
            output += f"{product[1]} {product[2]} {product[3]} {product[4]} {product[5]} {product[6]}\n"
        return output

# Function to delete a product by name and price
def delete_product(name, price):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_PRODUCT, (name, price))
        conn.commit()
        c.close()

# Example usage
if __name__ == "_main_":
    create_product_page_table()  # Create the table if it doesn't exist


    # Insert some products
    insert_product("Product A", "Description A", "Capacity A", 10.99, True, "1 year")
    insert_product("Product B", "Description B", "Capacity B", 15.49, True, "6 months")

    # Select and print all products
    print("All Products:")
    print(select_all_products())

    # Select and print a specific product
    print("\nProduct A with price 10.99:")
    print(select_product_by_name_and_price("Product A", 10.99))

    # Delete a product
    delete_product("Product A", 10.99)
    print("\nAll Products after deleting Product A:")
    print(select_all_products())