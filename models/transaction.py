from app.extensions import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    amount = db.Column(db.Integer)   # credits added
    method = db.Column(db.String(50))  # manual / jazzcash / easypaisa

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
