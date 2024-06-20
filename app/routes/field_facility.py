from flask import request, jsonify
from app import app, db
from app.models import Field, Facility, FieldFacility

@app.route('/field_facilities', methods=['POST', 'GET'])
def manage_field_facilities():
    if request.method == 'POST':
        data = request.json
        field_id = data.get('field_id')
        facility_id = data.get('facility_id')

        field = Field.query.get(field_id)
        if not field:
            return jsonify({"error": f"Field with ID {field_id} not found"}), 404

        facility = Facility.query.get(facility_id)
        if not facility:
            return jsonify({"error": f"Facility with ID {facility_id} not found"}), 404

        # Check if the association already exists
        existing_field_facility = FieldFacility.query.filter_by(field_id=field_id, facility_id=facility_id).first()
        if existing_field_facility:
            return jsonify({"message": "Field Facility association already exists"}), 400

        new_field_facility = FieldFacility(field_id=field_id, facility_id=facility_id)
        db.session.add(new_field_facility)
        db.session.commit()
        return jsonify({"message": "Field Facility association created successfully"}), 201
    
    elif request.method == 'GET':
        field_facilities = FieldFacility.query.all()
        field_facilities_list = [{"id": ff.id, "field_id": ff.field_id, "facility_id": ff.facility_id} for ff in field_facilities]
        return jsonify(field_facilities_list), 200
