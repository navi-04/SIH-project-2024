import sqlite3

# SQL queries
CREATE_CONSUMERS_TABLE = '''
CREATE TABLE IF NOT EXISTS consumers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    phonenumber TEXT,
    buyed_products TEXT,
    prebooked_products TEXT
);
'''

INSERT_CONSUMER = '''
INSERT INTO consumers (email, password, phonenumber, buyed_products, prebooked_products) 
VALUES (?, ?, ?, ?, ?);
'''

SELECT_ALL_CONSUMERS = '''
SELECT * FROM consumers;
'''

SELECT_CONSUMER = '''
SELECT * FROM consumers WHERE email = ? AND password = ?;
'''

DELETE_CONSUMER = '''
DELETE FROM consumers WHERE email = ? AND password = ?;
'''

# Create the consumers table
def create_consumers_table():
    conn = sqlite3.connect('consumers.db')
    with conn:
        conn.execute(CREATE_CONSUMERS_TABLE)
    conn.close()
    print("Table 'consumers' created successfully.")

# Insert a new consumer into the table
def insert_consumer(email, password, phonenumber, buyed_products, prebooked_products):
    conn = sqlite3.connect('consumers.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_CONSUMER, (email, password, phonenumber, buyed_products, prebooked_products))
        conn.commit()
        c.close()
    print("Consumer inserted successfully.")

# Select all consumers from the table
def select_all_consumers():
    conn = sqlite3.connect('consumers.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_CONSUMERS)
        consumers_list = c.fetchall()
        c.close()
    output = ''
    for consumer in consumers_list:
        output += f"Email: {consumer[1]}, Phone Number: {consumer[3]}, Buyed Products: {consumer[4]}, Prebooked Products: {consumer[5]}\n"
    return output

# Select a specific consumer by email and password
def select_consumer(email, password):
    conn = sqlite3.connect('consumers.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_CONSUMER, (email, password))
        consumer = c.fetchall()
        c.close()
    output = ''
    for x in consumer:
        output += f"Email: {x[1]}, Phone Number: {x[3]}, Buyed Products: {x[4]}, Prebooked Products: {x[5]}\n"
    return output

# Delete a consumer by email and password
def delete_consumer(email, password):
    conn = sqlite3.connect('consumers.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_CONSUMER, (email, password))
        conn.commit()
        c.close()
    print("Consumer deleted successfully.")

# Example Usage
if __name__ == "_main_":
    create_consumers_table()
    
    # Insert some example consumers
    insert_consumer("example1@example.com", "password123", "1234567890", "Apples, Bananas", "Oranges")
    insert_consumer("example2@example.com", "password456", "0987654321", "Tomatoes, Potatoes", "Cucumbers")

    # Select and print all consumers
    print(select_all_consumers())

    # Select a specific consumer
    print(select_consumer("example1@example.com", "password123"))

    # Delete a specific consumer
    delete_consumer("example2@example.com", "password456")

    # Select and print all consumers again to see the changes
    print(select_all_consumers())