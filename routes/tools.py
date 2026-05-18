from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

tools_bp = Blueprint("tools", __name__, url_prefix="/api/v1")

TOOLS = [
    {"id": 1, "name": "AI Writer", "category": "Content", "url": "https://chat.openai.com"},
    {"id": 2, "name": "SEO Tool", "category": "Marketing", "url": "https://ahrefs.com"}
]

@tools_bp.route("/tools", methods=["GET"])
@jwt_required()
def get_tools():
    return jsonify({
        "tools": TOOLS
    })
