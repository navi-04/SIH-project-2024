import sqlite3

# SQL Command to create the FarmerRequests table
CREATE_FARMER_REQUESTS = '''
CREATE TABLE IF NOT EXISTS FarmerRequests (
    RequestID INTEGER PRIMARY KEY AUTOINCREMENT,
    ConsumerName TEXT NOT NULL,
    ConsumerEmail TEXT NOT NULL,
    ConsumerPhoneNumber TEXT NOT NULL,
    ConsumerRequest TEXT NOT NULL,
    DeliveryDateTime TEXT NOT NULL
);
'''

# SQL Commands for inserting, selecting, and deleting records
INSERT_FARMER_REQUEST = "INSERT INTO FarmerRequests (ConsumerName, ConsumerEmail, ConsumerPhoneNumber, ConsumerRequest, DeliveryDateTime) VALUES (?, ?, ?, ?, ?);"
SELECT_ALL_REQUESTS = "SELECT * FROM FarmerRequests;"
SELECT_REQUEST = "SELECT * FROM FarmerRequests WHERE RequestID = ?;"
DELETE_REQUEST = "DELETE FROM FarmerRequests WHERE RequestID = ?;"

# Function to create the FarmerRequests table
def create_farmer_requests_table():
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        conn.execute(CREATE_FARMER_REQUESTS)
    conn.close()
    print("FarmerRequests table created successfully.")

# Function to insert a record into FarmerRequests
def insert_farmer_request(consumer_name, consumer_email, consumer_phone_number, consumer_request, delivery_date_time):
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_FARMER_REQUEST, (consumer_name, consumer_email, consumer_phone_number, consumer_request, delivery_date_time))
        conn.commit()
    conn.close()

# Function to select all records from FarmerRequests
def select_all_requests():
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
<<<<<<< Updated upstream
        c.execute('SELECT * FROM FarmerRequests')
        rows = c.fetchall()
        output = ''
        for row in rows:
            output += (f"ID: {row[0]}, ConsumerName: {row[1]}, Email: {row[2]}, PhoneNumber: {row[3]}, "
                       f"ProductRequested: {row[4]}, RequestedDeliveryDate: {row[5]}, RequestedDeliveryTime: {row[6]}\n")
=======
        c.execute(SELECT_ALL_REQUESTS)
        records = c.fetchall()
>>>>>>> Stashed changes
    conn.close()
    return records

<<<<<<< Updated upstream
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
=======
# Function to select a specific record by RequestID
def select_request(request_id):
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_REQUEST, (request_id,))
        record = c.fetchone()
>>>>>>> Stashed changes
    conn.close()
    return record

<<<<<<< Updated upstream
# Delete a record from FarmerRequests table by ID
def delete_farmer_request(request_id):
=======
# Function to delete a specific record by RequestID
def delete_request(request_id):
>>>>>>> Stashed changes
    conn = sqlite3.connect('farmer_requests.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_REQUEST, (request_id,))
        conn.commit()
    conn.close()

# Example usage
if _name_ == "_main_":
    create_farmer_requests_table()
<<<<<<< Updated upstream
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
=======
    # Insert a sample record
    insert_farmer_request('John Doe', 'john.doe@example.com', '123-456-7890', 'Request for organic vegetables', '2024-09-10 15:00:00')
    # Retrieve and print all records
    requests = select_all_requests()
    print(requests)
    # Retrieve and print a specific record
    request = select_request(1)
    print(request)
    # Delete a record
    delete_request(1)
>>>>>>> Stashed changes
