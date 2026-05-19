from app.extensions import db
from datetime import datetime

class APILog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    endpoint = db.Column(db.String(255))

    status_code = db.Column(db.Integer)

    response_time = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
