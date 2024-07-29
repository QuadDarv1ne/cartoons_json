from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cartoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)  # Поле для хранения URL изображения
    video = db.Column(db.String(200), nullable=True)  # Поле для хранения URL видео

    def __repr__(self):
        return '<Cartoon %r>' % self.title