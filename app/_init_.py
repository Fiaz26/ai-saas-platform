from flask import Flask
from .config import Config
from .extensions import db, jwt

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # Blueprints
    from .routes.auth import auth_bp
    from .routes.tools import tools_bp
    from .routes.admin import admin_bp
    from .routes.billing import billing_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tools_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(billing_bp)

    # Pages
    from flask import render_template

    @app.route("/")
    def home():
        return render_template("login.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    return app
