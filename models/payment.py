from app.extensions import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)
    amount = db.Column(db.Float)

    method = db.Column(db.String(50))  # jazzcash, easypaisa, bank
    status = db.Column(db.String(20), default="pending")

    transaction_id = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
