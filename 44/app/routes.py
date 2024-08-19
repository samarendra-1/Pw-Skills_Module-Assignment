# app/routes.py
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
