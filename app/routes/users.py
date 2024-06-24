from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app, db
from app.models import User  # Assuming User model is imported correctly

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        phone_number=data['phone_number'],
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role
        }
        for user in users
    ]
    return jsonify(users_list), 200

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    if user:
        user.username = data.get('username', user.username)
        user.password = data.get('password', user.password)
        user.email = data.get('email', user.email)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.role = data.get('role', user.role)
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        access_token = create_access_token(identity=user.username)
        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# User profile route
@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_username = get_jwt_identity()
    user = User.query.filter_by(username=current_user_username).first()
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email, "phone_number": user.phone_number, "role": user.role}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Endpoint to handle user document uploads
@app.route('/users/<int:user_id>/documents', methods=['POST'])
@jwt_required()
def upload_user_document(user_id):
    current_user_username = get_jwt_identity()
    if current_user_username:
        user = User.query.filter_by(username=current_user_username).first()
        if user and user.id == user_id:
            return jsonify({"message": "Document uploaded successfully"}), 200
        else:
            return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Authorization token missing"}), 401