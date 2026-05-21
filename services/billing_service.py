from app.extensions import db
from app.models.user import User
from app.models.transaction import Transaction
from app.models.usage_log import UsageLog
from app.models.user import User
from extensions import db
class BillingService:

    @staticmethod
    def add_credits(user_id, amount, method="manual"):

        user = User.query.get(user_id)
        user.credits += amount

        tx = Transaction(
            user_id=user_id,
            amount=amount,
            method=method
        )

        db.session.add(tx)
        db.session.commit()

        return user.credits

    @staticmethod
    

def deduct_credits(user_id, amount):
    user = User.query.get(user_id)

    if not user:
        return False, "User not found"

    if user.credits < amount:
        return False, "Insufficient credits"

    user.credits -= amount

    db.session.commit()

    return True, user.credits

        log = UsageLog(
            user_id=user_id,
            tool_name=tool_name,
            credits_used=cost
        )

        db.session.add(log)
        db.session.commit()

        return True
