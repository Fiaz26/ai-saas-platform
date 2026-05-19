from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.subscription_service import SubscriptionService

subscription_bp = Blueprint("subscriptions", __name__)

@subscription_bp.route("/subscribe", methods=["POST"])
@jwt_required()
def subscribe():

    user_id = get_jwt_identity()

    plan = request.json.get("plan")

    sub = SubscriptionService.create_subscription(
        user_id,
        plan
    )

    if not sub:
        return jsonify({
            "error": "Invalid plan"
        }), 400

    return jsonify({
        "message": "Subscription activated",
        "plan": plan
    })
