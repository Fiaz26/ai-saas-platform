from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.billing_service import BillingService

billing_bp = Blueprint("billing", __name__)

@billing_bp.route("/credits")
@jwt_required()
def get_credits():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "credits": user.credits
    })


@billing_bp.route("/add-demo-credits")
@jwt_required()
def add_demo_credits():

    user_id = get_jwt_identity()

    new_balance = BillingService.add_credits(user_id, 50, "manual")

    return jsonify({
        "message": "Credits added",
        "balance": new_balance
    })
