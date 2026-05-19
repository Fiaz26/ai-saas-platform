from flask_jwt_extended import get_jwt_identity

def user_rate_limit():
    try:
        return str(get_jwt_identity())
    except:
        return "anonymous"
      from app.utils.rate_limit_key import user_rate_limit
