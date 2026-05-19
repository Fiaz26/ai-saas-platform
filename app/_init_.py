from flask import Flask
from config import Config
from extensions import db, jwt

from routers.users import users_bp
from routers.tools import tools_bp
from routers.admin import admin_bp
from routers.billing import billing_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    return app

    # blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(tools_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(billing_bp)

    # pages
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app

