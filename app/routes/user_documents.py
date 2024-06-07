from flask import request, jsonify
from app import app, db
from app.models import UserDocument

from flask import request

@app.route('/user_documents', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_user_documents():
    if request.method == 'POST':
        data = request.json
        new_user_document = UserDocument(user_id=data['user_id'], document_number=data['document_number'], expiry_date=data['expiry_date'])
        db.session.add(new_user_document)
        db.session.commit()
        return jsonify({"message": "User document created successfully"}), 201
    
    elif request.method == 'GET':
        user_documents = UserDocument.query.all()
        user_documents_list = [{"id": user_document.id, "user_id": user_document.user_id, "document_number": user_document.document_number, "expiry_date": user_document.expiry_date} for user_document in user_documents]
        return jsonify(user_documents_list), 200

    elif request.method == 'PUT':
        data = request.json
        user_document_id = data.get('id')
        user_document = UserDocument.query.get(user_document_id)
        if user_document:
            user_document.user_id = data.get('user_id', user_document.user_id)
            user_document.document_number = data.get('document_number', user_document.document_number)
            user_document.expiry_date = data.get('expiry_date', user_document.expiry_date)
            db.session.commit()
            return jsonify({"message": "User document updated successfully"}), 200
        else:
            return jsonify({"error": "User document not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        user_document_id = data.get('id')
        user_document = UserDocument.query.get(user_document_id)
        if user_document:
            db.session.delete(user_document)
            db.session.commit()
            return jsonify({"message": "User document deleted successfully"}), 200
        else:
            return jsonify({"error": "User document not found"}), 404
