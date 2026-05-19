from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

tools_bp = Blueprint("tools", __name__)

@tools_bp.route("/")
@jwt_required()
def get_tools():

    tools = [
        {
            "name": "AI Writer",
            "category": "Content",
            "url": "https://chat.openai.com"
        }
    ]

    return jsonify(tools)
