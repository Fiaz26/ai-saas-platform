from app.models.subscription import Subscription
from datetime import datetime

def has_active_subscription(user_id):

    sub = Subscription.query.filter_by(
        user_id=user_id,
        status="active"
    ).first()

    if not sub:
        return False

    if sub.expires_at < datetime.utcnow():
        sub.status = "expired"
        return False

    return True
