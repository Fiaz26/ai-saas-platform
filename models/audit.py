from app.extensions import db

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)
    action = db.Column(db.String(255))

    meta = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, server_default=db.func.now())
