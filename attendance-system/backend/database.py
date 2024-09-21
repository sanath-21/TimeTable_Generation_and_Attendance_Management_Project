from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10))  # 'teacher' or 'student'
    phone_number = db.Column(db.String(20))

# Include other models similarly...
