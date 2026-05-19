from app.extensions import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.String(120), unique=True)

    amount = db.Column(db.Integer)
    status = db.Column(db.String(50))  # success / failed / pending

    provider = db.Column(db.String(50))  # jazzcash

    txn_ref = db.Column(db.String(120))
    raw_response = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
