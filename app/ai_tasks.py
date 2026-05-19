from app import celery
import time

@celery.task(bind=True)
def run_ai_task(self, prompt, api_name):

    try:

        # simulate AI processing
        time.sleep(5)

        result = f"AI result for: {prompt}"

        return {
            "status": "completed",
            
            "result": result,
            "api": api_name
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.tasks.ai_tasks import run_ai_task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/run", methods=["POST"])
@jwt_required()
def run_task():

    data = request.json

    prompt = data.get("prompt")
    api_name = data.get("api")

    task = run_ai_task.delay(prompt, api_name)

    return jsonify({
        "task_id": task.id,
        "status": "queued"
    })
