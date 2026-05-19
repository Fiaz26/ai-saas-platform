from app.extensions import db
from datetime import datetime

class VendorRevenue(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(db.Integer)

    api_id = db.Column(db.Integer)

    amount = db.Column(db.Float)

    platform_fee = db.Column(db.Float)

    vendor_earning = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
