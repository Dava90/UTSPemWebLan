from config import app, db
from routes.Game_bp import game_bp
from routes.Genre_bp import genre_bp
from routes.Developer_bp import developer_bp

app.register_blueprint(game_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(developer_bp)
db.create_all()
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
