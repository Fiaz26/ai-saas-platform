from app.extensions import db

class VendorWallet(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(
        db.Integer,
        unique=True
    )

    balance = db.Column(
        db.Float,
        default=0
    )

    pending_balance = db.Column(
        db.Float,
        default=0
    )

    lifetime_earnings = db.Column(
        db.Float,
        default=0
    )
