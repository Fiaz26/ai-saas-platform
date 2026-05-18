from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.billing_service import deduct_credits
from app.services.usage_service import log_usage

tools_bp = Blueprint("tools", __name__, url_prefix="/api/v1")


TOOLS = [
    {"id": 1, "name": "AI Writer"},
    {"id": 2, "name": "SEO Analyzer"}
]


@tools_bp.route("/tools", methods=["GET"])
@jwt_required()
def get_tools():

    user = get_jwt_identity()

    return jsonify(TOOLS)


@tools_bp.route("/tools/use", methods=["POST"])
@jwt_required()
def use_tool():

    user = get_jwt_identity()

    # CREDIT CHECK
    if not deduct_credits(user["user_id"], 1):
        return {"error": "No credits"}, 403

    log_usage(user["user_id"], "AI Tool")

    return {"message": "Tool executed successfully"}
