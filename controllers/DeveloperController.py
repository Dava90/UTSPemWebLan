from flask import jsonify, request
from models.DeveloperModel import Developer
from config import db

def get_developers():
    developers = Developer.query.all()
    return jsonify([developer.to_dict() for developer in developers])

def get_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404
    return jsonify(developer.to_dict())

def add_developer():
    data = request.get_json()
    developer = Developer(name=data['name'], country=data['country'])
    db.session.add(developer)
    db.session.commit()
    return jsonify({'message': 'Developer added successfully!', 'developer': developer.to_dict()}), 201

def update_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404

    data = request.get_json()
    developer.name = data.get('name', developer.name)
    developer.country = data.get('country', developer.country)

    db.session.commit()
    return jsonify({'message': 'Developer updated successfully!', 'developer': developer.to_dict()})

def patch_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'error': 'Developer not found'}), 404

    updated_data = request.get_json()

    # Update hanya data yang ada di request
    if 'name' in updated_data:
        developer.name = updated_data['name']
    if 'country' in updated_data:
        developer.country = updated_data['country']

    db.session.commit()
    return jsonify({'message': 'Developer updated successfully!', 'developer': developer.to_dict()})


def delete_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404

    db.session.delete(developer)
    db.session.commit()
    return jsonify({'message': 'Developer deleted successfully!'})
