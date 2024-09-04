import sqlite3

# SQL Commands
CREATE_PRODUCT_STATUS = '''
CREATE TABLE IF NOT EXISTS product_status (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    mark_as_unavailable BOOLEAN NOT NULL
);
'''

INSERT_PRODUCT_STATUS = '''
INSERT INTO product_status (product_name, mark_as_unavailable)
VALUES (?, ?);
'''

SELECT_ALL_PRODUCTS = '''
SELECT * FROM product_status;
'''

SELECT_PRODUCT_BY_NAME = '''
SELECT * FROM product_status WHERE product_name = ?;
'''

DELETE_PRODUCT = '''
DELETE FROM product_status WHERE product_name = ?;
'''

# Function to create the product_status table
def create_product_status_table():
    conn = sqlite3.connect('products.db')
    with conn:
        conn.execute(CREATE_PRODUCT_STATUS)

# Function to insert a product into the product_status table
def insert_product(product_name, mark_as_unavailable):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_PRODUCT_STATUS, (product_name, mark_as_unavailable))
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
            output += f"{product[1]} Unavailable: {product[2]}\n"
        return output

# Function to select a specific product by name
def select_product_by_name(product_name):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_PRODUCT_BY_NAME, (product_name,))
        # Store data into a list of tuples
        products = c.fetchall()
        c.close()
        output = ''
        for product in products:
            output += f"{product[1]} Unavailable: {product[2]}\n"
        return output

# Function to delete a product by name
def delete_product(product_name):
    conn = sqlite3.connect('products.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_PRODUCT, (product_name,))
        conn.commit()
        c.close()

# Example usage
if __name__ == "_main_":
    create_product_status_table()  # Create the table if it doesn't exist

    # Insert some products
    insert_product("Product A", True)
    insert_product("Product B", False)

    # Select and print all products
    print("All Products:")
    print(select_all_products())

    # Select and print a specific product
    print("\nProduct A:")
    print(select_product_by_name("Product A"))

    # Delete a product
    delete_product("Product A")
    print("\nAll Products after deleting Product A:")
    print(select_all_products())