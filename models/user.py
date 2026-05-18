from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="user")  # user / admin

    credits = db.Column(db.Integer, default=100)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
