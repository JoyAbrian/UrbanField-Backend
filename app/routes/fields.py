from flask import request, jsonify
from app import app, db
from app.models import Field, FieldType

@app.route('/fields', methods=['POST', 'GET'])
@app.route('/fields/<int:field_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_fields(field_id=None):
    if request.method == 'POST':
        data = request.json
        new_field = Field(
            name=data['name'],
            type_id=data['type_id'],
            city=data['city'],
            address=data['address'],
            street_address=data.get('street_address'),
            image_url=data.get('image_url'),
            image_url2=data.get('image_url2'),
            image_url3=data.get('image_url3'),
            price_per_hour=data['price_per_hour'],
            opening_time=data.get('opening_time'),
            closing_time=data.get('closing_time'),
        )
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
        data = request.json
        field = Field.query.get(field_id)
        if field:
            field.name = data.get('name', field.name)
            field.type_id = data.get('type_id', field.type_id)
            field.city = data.get('city', field.city)
            field.address = data.get('address', field.address)
            field.street_address = data.get('street_address', field.street_address)
            field.image_url = data.get('image_url', field.image_url)
            field.image_url2 = data.get('image_url2', field.image_url2)
            field.image_url3 = data.get('image_url3', field.image_url3)
            field.price_per_hour = data.get('price_per_hour', field.price_per_hour)
            field.opening_time = data.get('opening_time', field.opening_time)
            field.closing_time = data.get('closing_time', field.closing_time)
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