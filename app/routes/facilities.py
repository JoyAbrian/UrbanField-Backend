from flask import request, jsonify
from app import app, db
from app.models import Facility

@app.route('/facilities', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_facilities():
    if request.method == 'POST':
        data = request.json
        new_facility = Facility(name=data['name'], icon=data['icon'])
        db.session.add(new_facility)
        db.session.commit()
        return jsonify({"message": "Facility created successfully"}), 201
    
    elif request.method == 'GET':
        facilities = Facility.query.all()
        facilities_list = [{"id": facility.id, "name": facility.name, "icon": facility.icon} for facility in facilities]
        return jsonify(facilities_list), 200

    elif request.method == 'PUT':
        data = request.json
        facility_id = data.get('id')
        facility = Facility.query.get(facility_id)
        if facility:
            facility.name = data.get('name', facility.name)
            facility.icon = data.get('icon', facility.icon)
            db.session.commit()
            return jsonify({"message": "Facility updated successfully"}), 200
        else:
            return jsonify({"error": "Facility not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        facility_id = data.get('id')
        facility = Facility.query.get(facility_id)
        if facility:
            db.session.delete(facility)
            db.session.commit()
            return jsonify({"message": "Facility deleted successfully"}), 200
        else:
            return jsonify({"error": "Facility not found"}), 404