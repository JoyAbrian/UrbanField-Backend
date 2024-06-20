from flask import request, jsonify
from app import app, db
from app.models import Booking, User, Field, PaymentMethod

@app.route('/bookings', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_bookings():
    if request.method == 'POST':
        data = request.json
        new_booking = Booking(
            user_id=data['user_id'],
            field_id=data['field_id'],
            date=data['date'],
            time=data['time'],
            payment_method_id=data['payment_method_id']
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully"}), 201
    
    elif request.method == 'GET':
        bookings = Booking.query.all()
        bookings_list = [
            {
                "id": booking.id,
                "user_id": booking.user_id,
                "field_id": booking.field_id,
                "date": booking.date,
                "time": booking.time,
                "payment_method_id": booking.payment_method_id
            }
            for booking in bookings
        ]
        return jsonify(bookings_list), 200

    elif request.method == 'PUT':
        data = request.json
        booking_id = data.get('id')
        booking = Booking.query.get(booking_id)
        if booking:
            booking.user_id = data.get('user_id', booking.user_id)
            booking.field_id = data.get('field_id', booking.field_id)
            booking.date = data.get('date', booking.date)
            booking.time = data.get('time', booking.time)
            booking.payment_method_id = data.get('payment_method_id', booking.payment_method_id)
            db.session.commit()
            return jsonify({"message": "Booking updated successfully"}), 200
        else:
            return jsonify({"error": "Booking not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        booking_id = data.get('id')
        booking = Booking.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return jsonify({"message": "Booking deleted successfully"}), 200
        else:
            return jsonify({"error": "Booking not found"}), 404