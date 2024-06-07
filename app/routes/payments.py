from flask import request, jsonify
from app import app, db
from app.models import Payment

@app.route('/payments', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_payments():
    if request.method == 'POST':
        data = request.json
        new_payment = Payment(booking_id=data['booking_id'], amount=data['amount'], payment_date=data['payment_date'])
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"message": "Payment created successfully"}), 201
    
    elif request.method == 'GET':
        payments = Payment.query.all()
        payments_list = [{"id": payment.id, "booking_id": payment.booking_id, "amount": payment.amount, "payment_date": payment.payment_date} for payment in payments]
        return jsonify(payments_list), 200

    elif request.method == 'PUT':
        data = request.json
        payment_id = data.get('id')
        payment = Payment.query.get(payment_id)
        if payment:
            payment.booking_id = data.get('booking_id', payment.booking_id)
            payment.amount = data.get('amount', payment.amount)
            payment.payment_date = data.get('payment_date', payment.payment_date)
            db.session.commit()
            return jsonify({"message": "Payment updated successfully"}), 200
        else:
            return jsonify({"error": "Payment not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        payment_id = data.get('id')
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return jsonify({"message": "Payment deleted successfully"}), 200
        else:
            return jsonify({"error": "Payment not found"}), 404
