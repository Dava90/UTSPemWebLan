from flask import jsonify, request
from models.GameModel import Game
from models.GenreModel import Genre
from models.DeveloperModel import Developer
from config import db

def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

def get_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404
    return jsonify(game.to_dict())

def add_game():
    data = request.get_json()
    game = Game(
        name=data['name'],
        release=data['release'],
        rating=data['rating'],
        genre_id=data['genre_id'],
        developer_id=data['developer_id']
    )
    db.session.add(game)
    db.session.commit()
    return jsonify({'message': 'Game added successfully!', 'game': game.to_dict()}), 201

def update_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    data = request.get_json()
    game.name = data.get('name', game.name)
    game.release = data.get('release', game.release)
    game.rating = data.get('rating', game.rating)
    game.genre_id = data.get('genre_id', game.genre_id)
    game.developer_id = data.get('developer_id', game.developer_id)

    db.session.commit()
    return jsonify({'message': 'Game updated successfully!', 'game': game.to_dict()})

def patch_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    data = request.get_json()

    if 'name' in data:
        game.name = data['name']
    if 'release' in data:
        game.release = data['release']
    if 'rating' in data:
        game.rating = data['rating']
    if 'genre_id' in data:
        game.genre_id = data['genre_id']
    if 'developer_id' in data:
        game.developer_id = data['developer_id']

    db.session.commit()
    return jsonify({'message': 'Game updated successfully!', 'game': game.to_dict()})

def delete_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully!'})
