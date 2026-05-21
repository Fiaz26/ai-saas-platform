
from app.extensions import db
from datetime import datetime

class Payout(db.Model):
    __tablename__ = "payouts"

    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(db.Integer, db.ForeignKey("vendors.id"))

    amount = db.Column(db.Integer)

    status = db.Column(db.String(20), default="pending")
    # pending | paid | failed

    method = db.Column(db.String(50))  # JazzCash, bank, etc.

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
