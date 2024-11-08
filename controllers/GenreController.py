from flask import jsonify, request
from models.GenreModel import Genre
from config import db

def get_genres():
    genres = Genre.query.all()
    return jsonify([genre.to_dict() for genre in genres])

def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404
    return jsonify(genre.to_dict())

def add_genre():
    data = request.get_json()
    genre = Genre(name=data['name'])
    db.session.add(genre)
    db.session.commit()
    return jsonify({'message': 'Genre added successfully!', 'genre': genre.to_dict()}), 201

def update_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404

    data = request.get_json()
    genre.name = data.get('name', genre.name)

    db.session.commit()
    return jsonify({'message': 'Genre updated successfully!', 'genre': genre.to_dict()})

def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404

    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre deleted successfully!'})
