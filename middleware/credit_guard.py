from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify

from app.services.subscription_service import (
    get_user_subscription,
    can_use_api,
    increment_usage
)

def api_limit_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):

            verify_jwt_in_request()

            user_id = get_jwt_identity()

            sub = get_user_subscription(user_id)

            if not sub:
                return jsonify({
                    "error": "No subscription"
                }), 403

            if not can_use_api(sub):
                return jsonify({
                    "error": "API limit exceeded"
                }), 403

            increment_usage(sub)

            return fn(*args, **kwargs)

        return wrapper

    return decorator
