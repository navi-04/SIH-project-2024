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

<<<<<<< Updated upstream

=======
# Closing the connection after usage
>>>>>>> Stashed changes
connection.close()

