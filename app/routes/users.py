from flask import request, jsonify
from app import app, db
from app.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/users', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_users():
    if request.method == 'POST':
        data = request.json
        new_user = User(username=data['username'], password=data['password'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    
    elif request.method == 'GET':
        users = User.query.all()
        users_list = [{"id": user.id, "username": user.username, "role": user.role} for user in users]
        return jsonify(users_list), 200

    elif request.method == 'PUT':
        data = request.json
        user_id = data.get('id')
        user = User.query.get(user_id)
        if user:
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.role = data.get('role', user.role)
            db.session.commit()
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        user_id = data.get('id')
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:  # Assuming plaintext comparison for demonstration
        access_token = create_access_token(identity=user.username).decode('utf-8')
        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_username = get_jwt_identity()
    user = User.query.filter_by(username=current_user_username).first()
    return jsonify({"id": user.id, "username": user.username, "role": user.role}), 200