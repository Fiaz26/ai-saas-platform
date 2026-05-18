from app.models.user import User
from app.models.payment import Payment
from app.extensions import db

def add_credits(user_id, amount):

    user = User.query.get(user_id)
    user.credits += amount

    db.session.commit()


def deduct_credits(user_id, amount=1):

    user = User.query.get(user_id)

    if user.credits < amount:
        return False

    user.credits -= amount
    db.session.commit()

    return True
