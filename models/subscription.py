from app.extensions import db

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    plan = db.Column(db.String(50))  # free / pro / enterprise
    status = db.Column(db.String(20), default="active")

    stripe_customer_id = db.Column(db.String(255))
    stripe_subscription_id = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
