from app.extensions import db

class AIAPI(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))
    slug = db.Column(db.String(120), unique=True)

    category = db.Column(db.String(120))

    description = db.Column(db.Text)

    endpoint = db.Column(db.String(255))

    credit_cost = db.Column(db.Integer, default=1)

    active = db.Column(db.Boolean, default=True)
