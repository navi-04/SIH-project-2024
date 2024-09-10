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

INSERT_FARMER = "INSERT INTO farmers (email, address, password, phone_number, pincode, products) VALUES(?,?,?,?,?,?);"
SELECT_ALL_FARMERS = "SELECT * FROM farmers;"
SELECT_FARMER = "SELECT * FROM farmers WHERE email = ? AND phone_number = ?;"
DELETE_FARMER = "DELETE FROM farmers WHERE email = ? AND phone_number = ?;"


# Create the farmers table
def create_farmers_table():
    conn = sqlite3.connect('farmers.db')
    with conn:
        conn.execute(CREATE_FARMERS)

# Insert a new farmer into the table
def insert_farmer(email, address, password, phone_number, pincode, products):
    conn = sqlite3.connect('farmers.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_FARMER, (email, address, password, phone_number, pincode, products))
        conn.commit()
        c.close()

# Select all farmers from the table
def select_all_farmers():
    conn = sqlite3.connect('farmers.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_FARMERS)
        # Store data into a list of Tuples
        farmers_list = c.fetchall()
        c.close()
        output = ''
        for farmer in farmers_list:
            output += f"Email: {farmer[1]}, Address: {farmer[2]}, Phone: {farmer[4]}, Pincode: {farmer[5]}, Products: {farmer[6]}\n"
        return output

# Select a specific farmer based on email and phone number
def select_farmer(email, phone_number):
    conn = sqlite3.connect('farmers.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_FARMER, (email, phone_number))
        # Store data into a list of Tuples
        farmer = c.fetchall()
        c.close()
        output = ''
        for f in farmer:
            output += f"Email: {f[1]}, Address: {f[2]}, Phone: {f[4]}, Pincode: {f[5]}, Products: {f[6]}\n"
        return output

# Delete a farmer from the table based on email and phone number
def delete_farmer(email, phone_number):
    conn = sqlite3.connect('farmers.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_FARMER, (email, phone_number))
        conn.commit()
        c.close()

# Example usage
if __name__ == "_main_":
    # Create the table
    create_farmers_table()
    
    # Insert a new farmer
    insert_farmer("john@example.com", "123 Farm Road", "securepassword", "1234567890", "123456", "Wheat, Corn")

    # Select and print all farmers
    print("All Farmers:")
    print(select_all_farmers())

    # Select and print a specific farmer
    print("Specific Farmer:")
    print(select_farmer("john@example.com", "1234567890"))

    # Delete the farmer
    delete_farmer("john@example.com", "1234567890")
    
    # Verify deletion
    print("After Deletion:")
    print(select_all_farmers())