from database import db  # Import the db instance
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10))  # 'teacher' or 'student'
    phone_number = db.Column(db.String(20))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    status = db.Column(db.String(10))  # 'present' or 'absent'

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))
    day = db.Column(db.String(10))  # 'Monday', 'Tuesday', etc.
    time = db.Column(db.String(10))
    subject = db.Column(db.String(50))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
