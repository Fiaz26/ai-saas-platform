from functools import wraps
from flask import jsonify

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity
)

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

            subscription = get_user_subscription(user_id)

            if not subscription:
                return jsonify({
                    "error": "subscription not found"
                }), 404

            if not can_use_api(subscription):
                return jsonify({
                    "error": "API limit exceeded",
                    "plan": subscription.plan
                }), 403

            increment_usage(subscription)

            return fn(*args, **kwargs)

        return wrapper

    return decorator
