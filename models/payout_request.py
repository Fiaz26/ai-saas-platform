from app.extensions import db
from datetime import datetime

class PayoutRequest(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(db.Integer)

    amount = db.Column(db.Float)

    method = db.Column(db.String(50))
    # jazzcash / easypaisa / bank

    account_number = db.Column(db.String(120))

    status = db.Column(
        db.String(50),
        default="pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
