from flask import Flask
from config.base import Config
from app.extensions import db, jwt

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    # register blueprints
    from app.api.v1.auth import auth_bp
    from app.api.v1.tools import tools_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(tools_bp, url_prefix="/api/v1/tools")

    return app

