from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.revenue_service import RevenueService
from app import limiter
from app.models.ai_api import AIAPI
from app.services.billing_service import BillingService

execute_bp = Blueprint("execute", __name__)

@execute_bp.route("/<slug>", methods=["POST"])
@jwt_required()
def execute_api(slug):

    user_id = get_jwt_identity()

    api = AIAPI.query.filter_by(
        slug=slug,
        active=True
    ).first()

    if not api:
        return {"error": "API not found"}, 404
limiter = Limiter(
    key_func=user_rate_limit,
    default_limits=["1000 per day"]
)

    # deduct credits
    success = BillingService.deduct_credits(
        user_id=user_id,
        tool_name=api.name,
        cost=api.credit_cost
    )

    if not success:
        return {
            "error": "Insufficient credits"
        }, 403
RevenueService.distribute(
    api,
    api.credit_cost
)
    # fake AI response example
    prompt = request.json.get("prompt")

    result = {
        "api": api.name,
        "prompt": prompt,
        "response": f"AI generated result for: {prompt}"
    }

    return jsonify(result)
