from flask import Flask
from flask_cors import CORS
from database import db, User  # Import the db instance
from flask import request, jsonify
from flask_bcrypt import Bcrypt
import jwt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
db.init_app(app)  # Initialize the db with the app
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)






bcrypt = Bcrypt(app)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data['role'],
        phone_number=data['phone']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
