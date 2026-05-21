from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.tasks.ai_tasks import generate_ai_content
from app.services.billing_service import deduct_credits

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/api/generate", methods=["POST"])
@jwt_required()
def generate():

    data = request.json

    prompt = data.get("prompt")

    user_id = get_jwt_identity()

    # deduct credits
    success, result = deduct_credits(user_id, 5)

    if not success:
        return jsonify({"error": result}), 400

    # queue task
    task = generate_ai_content.delay(prompt, user_id)

    return jsonify({
        "task_id": task.id,
        "credits_left": result
    })
