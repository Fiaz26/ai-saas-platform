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
