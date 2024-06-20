from flask import request, jsonify
from app import app, db
from app.models import Field, User, FieldReview

@app.route('/field_reviews', methods=['POST', 'GET'])
def manage_field_reviews():
    if request.method == 'POST':
        data = request.json
        field_id = data.get('field_id')
        user_id = data.get('user_id')
        rating = data.get('rating')
        review = data.get('review')

        field = Field.query.get(field_id)
        if not field:
            return jsonify({"error": f"Field with ID {field_id} not found"}), 404

        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404

        new_field_review = FieldReview(field_id=field_id, user_id=user_id, rating=rating, review=review)
        db.session.add(new_field_review)
        db.session.commit()
        return jsonify({"message": "Field review created successfully"}), 201
    
    elif request.method == 'GET':
        field_reviews = FieldReview.query.all()
        field_reviews_list = [{"id": fr.id, "field_id": fr.field_id, "user_id": fr.user_id, "rating": fr.rating, "review": fr.review} for fr in field_reviews]
        return jsonify(field_reviews_list), 200