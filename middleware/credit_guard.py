from flask_jwt_extended import get_jwt_identity
from app.models.user import User

def has_credits(required=1):

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    return user.credits >= required
