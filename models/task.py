from app.extensions import db
from datetime import datetime

class AITask(db.Model):
    __tablename__ = "ai_tasks"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    task_id = db.Column(db.String(120))  # celery task id

    prompt = db.Column(db.Text)

    status = db.Column(db.String(20), default="pending")
    # pending | running | completed | failed

    result = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
