from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from app.services.subscription_service import (
    get_user_subscription,
    increment_usage
)


def api_limit_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        user_id = get_jwt_identity()

        sub = get_user_subscription(user_id)

        # If no subscription found
        if not sub:
            return jsonify({
                "error": "No active subscription"
            }), 403

        # FREE plan enforcement
        if sub.api_limit != -1 and sub.api_used >= sub.api_limit:
            return jsonify({
                "error": "API limit exceeded",
                "limit": sub.api_limit,
                "used": sub.api_used,
                "plan": sub.plan
            }), 403

        # Allow request first, then increment safely
        response = f(*args, **kwargs)

        try:
            increment_usage(user_id)
        except Exception:
            pass

        return response

    return decorated
