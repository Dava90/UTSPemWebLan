from config import db

class Developer(db.Model):
    developer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    games = db.relationship('Game', back_populates='developer')

    def to_dict(self):
        return {
            'developer_id': self.developer_id,
            'name': self.name,
            'country': self.country
        }
