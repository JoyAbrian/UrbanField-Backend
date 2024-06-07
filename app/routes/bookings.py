from flask import request, jsonify
from app import app, db
from app.models import Booking

from flask import request

@app.route('/bookings', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_bookings():
    if request.method == 'POST':
        data = request.json
        new_booking = Booking(user_id=data['user_id'], field_id=data['field_id'], start_date=data['start_date'], end_date=data['end_date'], total_price=data['total_price'])
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully"}), 201
    
    elif request.method == 'GET':
        bookings = Booking.query.all()
        bookings_list = [{"id": booking.id, "user_id": booking.user_id, "field_id": booking.field_id, "start_date": booking.start_date, "end_date": booking.end_date, "total_price": booking.total_price} for booking in bookings]
        return jsonify(bookings_list), 200

    elif request.method == 'PUT':
        data = request.json
        booking_id = data.get('id')
        booking = Booking.query.get(booking_id)
        if booking:
            booking.user_id = data.get('user_id', booking.user_id)
            booking.field_id = data.get('field_id', booking.field_id)
            booking.start_date = data.get('start_date', booking.start_date)
            booking.end_date = data.get('end_date', booking.end_date)
            booking.total_price = data.get('total_price', booking.total_price)
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
