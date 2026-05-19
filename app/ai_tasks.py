from app import celery
import time
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.tasks.ai_tasks import run_ai_task
from celery.result import AsyncResult
from app import celery
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
@tasks_bp.route("/status/<task_id>")
@jwt_required()
def task_status(task_id):

    task = AsyncResult(task_id, app=celery)

    return jsonify({
        "task_id": task_id,
        "state": task.state,
        "result": task.result
    })
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
