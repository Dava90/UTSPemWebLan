from config import db

class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    games = db.relationship('Game', back_populates='genre')

    def to_dict(self):
        return {
            'genre_id': self.genre_id,
            'name': self.name
        }
