from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def create_connection():
    connection = sqlite3.connect('database.db')
    return connection

# Initialize the database
def init_db():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS farmers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE,
                        phone TEXT,
                        password TEXT,
                        address TEXT,
                        pincode TEXT,
                        products TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS consumers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE,
                        phone TEXT,
                        password TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT,
                        capacity TEXT,
                        price TEXT,
                        duration TEXT)''')

    connection.commit()
    connection.close()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_type = data['userType']
    email = data['email']
    phone = data['phone']
    password = data['password']
    
    connection = create_connection()
    cursor = connection.cursor()

    if user_type == 'farmer':
        address = data['address']
        pincode = data['pincode']
        products = data['products']
        cursor.execute("INSERT INTO farmers (email, phone, password, address, pincode, products) VALUES (?, ?, ?, ?, ?, ?)",
                       (email, phone, password, address, pincode, products))
    else:
        cursor.execute("INSERT INTO consumers (email, phone, password) VALUES (?, ?, ?)",
                       (email, phone, password))
    
    connection.commit()
    connection.close()

    return jsonify({"success": True})

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data['email']
    password = data['password']

    connection = create_connection()
    cursor = connection.cursor()

    # Determine the user type based on email
    user_type = 'farmer' if cursor.execute("SELECT * FROM farmers WHERE email=? AND password=?", (email, password)).fetchone() else 'consumer'
    table_name = 'farmers' if user_type == 'farmer' else 'consumers'

    cursor.execute(f"SELECT * FROM {table_name} WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    connection.close()

    if user:
        return jsonify({"success": True, "userType": user_type})
    else:
        return jsonify({"success": False})

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    description = data['description']
    capacity = data['capacity']
    price = data['price']
    duration = data['duration']

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO products (name, description, capacity, price, duration) VALUES (?, ?, ?, ?, ?)",
                   (name, description, capacity, price, duration))
    connection.commit()
    connection.close()

    return jsonify({"success": True})

@app.route('/products', methods=['GET'])
def get_products():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    connection.close()

    return jsonify(products)

@app.route('/buy_product', methods=['POST'])
def buy_product():
    data = request.get_json()
    product_name = data['productName']
    capacity = data['capacity']
    date = data['date']

    # Here you can add logic to deduct the capacity from the product, and store the order in an orders table.

    return jsonify({"success": True})

@app.route('/pre_book_product', methods=['POST'])
def pre_book_product():
    data = request.get_json()
    product_name = data['productName']
    capacity = data['capacity']
    date = data['date']

    # Here you can add logic to store the pre-booked product in a separate table.

    return jsonify({"success": True})

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
