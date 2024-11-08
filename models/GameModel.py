from config import db

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    # Foreign keys
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.developer_id'), nullable=False)

    genre = db.relationship('Genre', back_populates='games')
    developer = db.relationship('Developer', back_populates='games')

    def to_dict(self):
        return {
            'game_id': self.game_id,
            'name': self.name,
            'release': self.release,
            'rating': self.rating,
            'genre': self.genre.name if self.genre else None,
            'developer': self.developer.name if self.developer else None
        }
