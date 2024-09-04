import sqlite3

# Create table if it doesn't exist
def create_farmer_requests_table():
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS FarmerRequests (
            RequestID INTEGER PRIMARY KEY AUTOINCREMENT,
            ConsumerName TEXT NOT NULL,
            Email TEXT NOT NULL,
            PhoneNumber TEXT NOT NULL,
            ProductRequested TEXT NOT NULL,
            RequestedDeliveryDate TEXT NOT NULL,
            RequestedDeliveryTime TEXT NOT NULL
        )
        ''')
    conn.close()

# Insert record into FarmerRequests table
def insert_farmer_request(consumer_name, email, phone_number, product_requested, requested_delivery_date, requested_delivery_time):
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute('''
        INSERT INTO FarmerRequests (ConsumerName, Email, PhoneNumber, ProductRequested, RequestedDeliveryDate, RequestedDeliveryTime)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (consumer_name, email, phone_number, product_requested, requested_delivery_date, requested_delivery_time))
        conn.commit()
    conn.close()

# Select all records from FarmerRequests table
def select_all_farmer_requests():
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute('SELECT * FROM FarmerRequests')
        rows = c.fetchall()
        output = ''
        for row in rows:
            output += (f"ID: {row[0]}, ConsumerName: {row[1]}, Email: {row[2]}, PhoneNumber: {row[3]}, "
                       f"ProductRequested: {row[4]}, RequestedDeliveryDate: {row[5]}, RequestedDeliveryTime: {row[6]}\n")
    conn.close()
    return output

# Select a specific record from FarmerRequests table by ID
def select_farmer_request_by_id(request_id):
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute('SELECT * FROM FarmerRequests WHERE RequestID = ?', (request_id,))
        row = c.fetchone()
        output = ''
        if row:
            output = (f"ID: {row[0]}, ConsumerName: {row[1]}, Email: {row[2]}, PhoneNumber: {row[3]}, "
                      f"ProductRequested: {row[4]}, RequestedDeliveryDate: {row[5]}, RequestedDeliveryTime: {row[6]}")
    conn.close()
    return output

# Delete a record from FarmerRequests table by ID
def delete_farmer_request(request_id):
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute('DELETE FROM FarmerRequests WHERE RequestID = ?', (request_id,))
        conn.commit()
    conn.close()

# Example usage:
if __name__ == '_main_':
    create_farmer_requests_table()
    # Insert example record
    insert_farmer_request('John Doe', 'john.doe@example.com', '123-456-7890', 'Apples', '2024-09-15', '10:00 AM')
    # Print all records
    print("All Farmer Requests:")
    print(select_all_farmer_requests())
    # Print a specific record by ID
    print("\nFarmer Request with ID 1:")
    print(select_farmer_request_by_id(1))
    # Delete a record by ID
    delete_farmer_request(1)
    print("\nAll Farmer Requests after deletion:")
    print(select_all_farmer_requests())