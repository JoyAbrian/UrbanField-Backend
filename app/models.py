from app import db
from sqlalchemy import Enum

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(Enum('admin', 'customer'), nullable=False)

class FieldType(db.Model):
    __tablename__ = 'field_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Field(db.Model):
    __tablename__ = 'fields'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('field_types.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    status = db.Column(Enum('available', 'booked'), nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('fields.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)

class Facility(db.Model):
    __tablename__ = 'facilities'
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.Integer, db.ForeignKey('fields.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

class UserDocument(db.Model):
    __tablename__ = 'user_document'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    document_number = db.Column(db.String(50), nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
