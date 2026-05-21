from app.extensions import db
from datetime import datetime

class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))
    category = db.Column(db.String(50))

    endpoint = db.Column(db.String(255))

    cost_per_use = db.Column(db.Integer, default=1)

    vendor_id = db.Column(db.Integer)

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
