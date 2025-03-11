from flask_login import UserMixin
from app import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    predictions = db.relationship('Prediction', backref='user', lazy=True)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    snoring_rate = db.Column(db.Float, nullable=False)
    respiratory_rate = db.Column(db.Float, nullable=False)
    body_temperature = db.Column(db.Float, nullable=False)
    blood_oxygen = db.Column(db.Float, nullable=False)
    limb_movement = db.Column(db.Float, nullable=False)
    eye_movement = db.Column(db.Float, nullable=False)
    sleep_hours = db.Column(db.Float, nullable=False)
    heart_rate = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)