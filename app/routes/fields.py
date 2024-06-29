from flask import Flask, request, jsonify, send_from_directory
from app import app, db
from app.models import Field, FieldType, Facility, FieldFacility, FieldReview
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
import uuid

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads/fields/')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/fields/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/fields', methods=['POST', 'GET'])
@app.route('/fields/<int:field_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_fields(field_id=None):
    if request.method == 'POST':
        data = request.form
        files = request.files

        new_field = Field(
            name=data['name'],
            type_id=data['type_id'],
            city=data['city'],
            address=data['address'],
            street_address=data.get('street_address'),
            price_per_hour=data['price_per_hour'],
            opening_time=data.get('opening_time'),
            closing_time=data.get('closing_time')
        )

        # Handle image uploads with unique filenames
        if 'image_url' in files and allowed_file(files['image_url'].filename):
            filename = secure_filename(files['image_url'].filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            files['image_url'].save(filepath)
            new_field.image_url = f'uploads/fields/{unique_filename}'

        if 'image_url2' in files and allowed_file(files['image_url2'].filename):
            filename = secure_filename(files['image_url2'].filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            files['image_url2'].save(filepath)
            new_field.image_url2 = f'uploads/fields/{unique_filename}'

        if 'image_url3' in files and allowed_file(files['image_url3'].filename):
            filename = secure_filename(files['image_url3'].filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            files['image_url3'].save(filepath)
            new_field.image_url3 = f'uploads/fields/{unique_filename}'

        db.session.add(new_field)
        db.session.commit()
        return jsonify({"message": "Field created successfully"}), 201

    elif request.method == 'GET':
        if field_id is not None:
            field = Field.query.get(field_id)
            if field:
                venue = FieldType.query.get(field.type_id)
                field_data = {
                    "id": field.id,
                    "name": field.name,
                    "type_id": field.type_id,
                    "venue": venue.name,
                    "city": field.city,
                    "address": field.address,
                    "street_address": field.street_address,
                    "image_url": field.image_url,
                    "image_url2": field.image_url2,
                    "image_url3": field.image_url3,
                    "price_per_hour": field.price_per_hour,
                    "opening_time": field.opening_time.strftime('%H:%M') if field.opening_time else None,
                    "closing_time": field.closing_time.strftime('%H:%M') if field.closing_time else None,
                }
                return jsonify(field_data), 200
            else:
                return jsonify({"error": "Field not found"}), 404
        
        else:
            fields = Field.query.all()
            fields_list = []
            for field in fields:
                venue = FieldType.query.get(field.type_id)
                field_data = {
                    "id": field.id,
                    "name": field.name,
                    "type_id": field.type_id,
                    "venue": venue.name,
                    "city": field.city,
                    "address": field.address,
                    "street_address": field.street_address,
                    "image_url": field.image_url,
                    "image_url2": field.image_url2,
                    "image_url3": field.image_url3,
                    "price_per_hour": field.price_per_hour,
                    "opening_time": field.opening_time.strftime('%H:%M') if field.opening_time else None,
                    "closing_time": field.closing_time.strftime('%H:%M') if field.closing_time else None,
                }
                fields_list.append(field_data)
            return jsonify(fields_list), 200

    elif request.method == 'PUT':
        data = request.form
        files = request.files
        field = Field.query.get(field_id)
        if field:
            field.name = data.get('name', field.name)
            field.type_id = data.get('type_id', field.type_id)
            field.city = data.get('city', field.city)
            field.address = data.get('address', field.address)
            field.street_address = data.get('street_address', field.street_address)
            field.price_per_hour = data.get('price_per_hour', field.price_per_hour)
            field.opening_time = data.get('opening_time', field.opening_time)
            field.closing_time = data.get('closing_time', field.closing_time)

            # Handle image uploads with unique filenames
            if 'image_url' in files and allowed_file(files['image_url'].filename):
                filename = secure_filename(files['image_url'].filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                files['image_url'].save(filepath)
                field.image_url = f'uploads/fields/{unique_filename}'

            if 'image_url2' in files and allowed_file(files['image_url2'].filename):
                filename = secure_filename(files['image_url2'].filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                files['image_url2'].save(filepath)
                field.image_url2 = f'uploads/fields/{unique_filename}'

            if 'image_url3' in files and allowed_file(files['image_url3'].filename):
                filename = secure_filename(files['image_url3'].filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                files['image_url3'].save(filepath)
                field.image_url3 = f'uploads/fields/{unique_filename}'

            db.session.commit()
            return jsonify({"message": "Field updated successfully"}), 200
        else:
            return jsonify({"error": "Field not found"}), 404

    elif request.method == 'DELETE':
        field = Field.query.get(field_id)
        if field:
            db.session.delete(field)
            db.session.commit()
            return jsonify({"message": "Field deleted successfully"}), 200
        else:
            return jsonify({"error": "Field not found"}), 404

@app.route('/fields/<int:field_id>/facilities', methods=['GET'])
def get_field_facilities(field_id):
    field = Field.query.get(field_id)
    if not field:
        return jsonify({"error": "Field not found"}), 404
    
    facilities = Facility.query.join(FieldFacility, Facility.id == FieldFacility.facility_id)\
        .filter(FieldFacility.field_id == field_id)\
        .all()
    
    facilities_list = [{"id": facility.id, "name": facility.name, "icon": facility.icon} for facility in facilities]
    return jsonify(facilities_list), 200

@app.route('/fields/<int:field_id>/reviews', methods=['GET'])
def get_field_reviews(field_id):
    reviews = FieldReview.query.filter_by(field_id=field_id).all()
    reviews_list = [{
        "id": review.id,
        "user_id": review.user_id,
        "rating": review.rating,
        "review": review.review
    } for review in reviews]
    return jsonify(reviews_list), 200