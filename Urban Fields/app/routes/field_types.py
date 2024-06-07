from flask import request, jsonify
from app import app, db
from app.models import FieldType

from flask import request

@app.route('/field_types', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_field_types():
    if request.method == 'POST':
        data = request.json
        new_field_type = FieldType(name=data['name'])
        db.session.add(new_field_type)
        db.session.commit()
        return jsonify({"message": "Field type created successfully"}), 201
    
    elif request.method == 'GET':
        field_types = FieldType.query.all()
        field_types_list = [{"id": field_type.id, "name": field_type.name} for field_type in field_types]
        return jsonify(field_types_list), 200

    elif request.method == 'PUT':
        data = request.json
        field_type_id = data.get('id')
        field_type = FieldType.query.get(field_type_id)
        if field_type:
            field_type.name = data.get('name', field_type.name)
            db.session.commit()
            return jsonify({"message": "Field type updated successfully"}), 200
        else:
            return jsonify({"error": "Field type not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        field_type_id = data.get('id')
        field_type = FieldType.query.get(field_type_id)
        if field_type:
            db.session.delete(field_type)
            db.session.commit()
            return jsonify({"message": "Field type deleted successfully"}), 200
        else:
            return jsonify({"error": "Field type not found"}), 404
