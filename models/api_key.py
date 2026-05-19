from app.extensions import db

class APIKey(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    key = db.Column(db.String(255), unique=True)

    active = db.Column(db.Boolean, default=True)
