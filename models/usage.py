from app.extensions import db

class Usage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tool_name = db.Column(db.String(100))

    credits_used = db.Column(db.Integer, default=1)

    timestamp = db.Column(db.DateTime, server_default=db.func.now())
