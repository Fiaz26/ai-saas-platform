from app.extensions import db
from datetime import datetime

class BillingTransaction(db.Model):
    __tablename__ = "billing_transactions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    type = db.Column(db.String(50))  
    # credit_purchase | deduction | refund

    amount = db.Column(db.Integer)

    description = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
