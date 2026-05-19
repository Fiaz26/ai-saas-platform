from app.extensions import db

class Vendor(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))

    email = db.Column(db.String(120), unique=True)

    company = db.Column(db.String(120))

    api_key = db.Column(db.String(255))

    active = db.Column(db.Boolean, default=True)
