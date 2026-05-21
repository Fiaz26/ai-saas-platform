from app import create_app
app = create_app()
app = create_app()
celery = app.celery
from app.routes.ai_routes import ai_bp
app.register_blueprint(ai_bp)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
