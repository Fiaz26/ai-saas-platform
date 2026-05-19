from datetime import datetime, timedelta

from app.extensions import db
from app.models.subscription import Subscription
from app.models.user import User

from app.config.plans import PLANS

class SubscriptionService:

    @staticmethod
    def create_subscription(user_id, plan_name):

        plan = PLANS.get(plan_name)

        if not plan:
            return False

        # remove old active plans
        old = Subscription.query.filter_by(
            user_id=user_id,
            status="active"
        ).first()

        if old:
            old.status = "expired"

        sub = Subscription(
            user_id=user_id,
            plan_name=plan_name,
            monthly_credits=plan["credits"],
            started_at=datetime.utcnow(),
            expires_at=datetime.utcnow() + timedelta(days=30)
        )

        db.session.add(sub)

        # add credits
        user = User.query.get(user_id)
        user.credits += plan["credits"]

        db.session.commit()

        return sub
