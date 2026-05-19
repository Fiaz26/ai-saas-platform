from extensions import db

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)

    category = db.Column(db.String(120))

    url = db.Column(db.String(500))
