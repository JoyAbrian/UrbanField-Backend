from flask import request, jsonify
from app import app, db
from app.models import Field

from flask import request

@app.route('/fields', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_fields():
    if request.method == 'POST':
        data = request.json
        new_field = Field(name=data['name'], type_id=data['type_id'], location=data['location'], size=data['size'], price_per_hour=data['price_per_hour'], status=data['status'])
        db.session.add(new_field)
        db.session.commit()
        return jsonify({"message": "Field created successfully"}), 201
    
    elif request.method == 'GET':
        fields = Field.query.all()
        fields_list = [{"id": field.id, "name": field.name, "type_id": field.type_id, "location": field.location, "size": field.size, "price_per_hour": field.price_per_hour, "status": field.status} for field in fields]
        return jsonify(fields_list), 200

    elif request.method == 'PUT':
        data = request.json
        field_id = data.get('id')
        field = Field.query.get(field_id)
        if field:
            field.name = data.get('name', field.name)
            field.type_id = data.get('type_id', field.type_id)
            field.location = data.get('location', field.location)
            field.size = data.get('size', field.size)
            field.price_per_hour = data.get('price_per_hour', field.price_per_hour)
            field.status = data.get('status', field.status)
            db.session.commit()
            return jsonify({"message": "Field updated successfully"}), 200
        else:
            return jsonify({"error": "Field not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        field_id = data.get('id')
        field = Field.query.get(field_id)
        if field:
            db.session.delete(field)
            db.session.commit()
            return jsonify({"message": "Field deleted successfully"}), 200
        else:
            return jsonify({"error": "Field not found"}), 404
