from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.billing_service import BillingService

tools_bp = Blueprint("tools", __name__)

@tools_bp.route("/")
@jwt_required()
def get_tools():

    user_id = get_jwt_identity()

    success = BillingService.deduct_credits(
        user_id=user_id,
        tool_name="AI Writer",
        cost=1
    )

    if not success:
        return jsonify({"error": "Insufficient credits"}), 403

    tools = [
        {
            "name": "AI Writer",
            "category": "Content",
            "url": "https://chat.openai.com"
        }
    ]

    return jsonify(tools)
