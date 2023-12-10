from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///findmydesk.db'
db = SQLAlchemy(app)


class Library(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  floors = db.relationship('Floor', backref='library', lazy=True)


class Floor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  library_id = db.Column(db.Integer,
                         db.ForeignKey('library.id'),
                         nullable=False)
  number = db.Column(db.String(10), nullable=False)
  map_image_url = db.Column(db.String(255), nullable=False)
  seats = db.relationship('Seat', backref='floor', lazy=True)


class Seat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)
  label = db.Column(db.String(10), nullable=False)
  top_position = db.Column(db.Float, nullable=False)
  left_position = db.Column(db.Float, nullable=False)
  available = db.Column(db.Boolean, default=True, nullable=False)
