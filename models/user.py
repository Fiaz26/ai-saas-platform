from extensions import db
from flask import Blueprint
users_bp = Blueprint("users", __name__)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    credits = db.Column(db.Integer, default=100)
