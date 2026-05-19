from app.extensions import db
from datetime import datetime

class APIUsage(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    api_name = db.Column(db.String(120))

    credits_used = db.Column(db.Integer)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
