from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import jwt
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
bcrypt = Bcrypt(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'attendance_management'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key

# Initialize MySQL
mysql = MySQL(app)

# Serve frontend files from the 'frontend' directory
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>', methods=['GET'])
def send_file(path):
    return send_from_directory('../frontend', path)

# Sign-up route
@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve data from form or JSON
    if request.form:
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        role = request.form['role']
    else:
        data = request.json
        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        password = data['password']
        role = data['role']
    
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Check if the user already exists
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM users WHERE email=%s", [email])
    user = cur.fetchone()

    if user:
        return jsonify({'message': 'User already exists'}), 400

    # Insert user into the database
    cur.execute(
        'INSERT INTO users (name, email, phone_number, password, role) VALUES (%s, %s, %s, %s, %s)',
        (name, email, phone_number, hashed_password, role)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User registered successfully'}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json if request.is_json else request.form
    email = data['email']
    password = data['password']

    # Fetch user data from MySQL database
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM users WHERE email = %s', [email])
    user = cur.fetchone()
    cur.close()

    if user and bcrypt.check_password_hash(user['password'], password):
        # Generate JWT token
        token = jwt.encode({'user_id': user['id'], 'role': user['role']}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return jsonify({"token": token, "role": user['role']}), 200
    elif user:
        return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "User not found. Please sign up."}), 404

# Test route to ensure the backend is running
@app.route('/test')
def test():
    return "Backend is running!", 200

if __name__ == '__main__':
    app.run(debug=True)
