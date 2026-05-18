from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db

tools_bp = Blueprint("tools", __name__, url_prefix="/api/v1")

TOOLS = [
    {"id": 1, "name": "AI Writer", "category": "Content"},
    {"id": 2, "name": "SEO Tool", "category": "Marketing"}
]

@tools_bp.route("/tools", methods=["GET"])
@jwt_required()
def get_tools():

    user_data = get_jwt_identity()
    user = User.query.get(user_data["user_id"])

    if user.credits <= 0:
        return jsonify({"error": "No credits left"}), 403

    return jsonify({
        "tools": TOOLS,
        "credits": user.credits
    })
