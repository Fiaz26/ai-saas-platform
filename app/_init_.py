from flask import Flask
from config.base import Config
from app.extensions import db, jwt
from app.middleware.logger import (
    before_request,
    after_request
)

app.before_request(before_request)
app.after_request(after_request)
from app.middleware.logger import (
    before_request,
    after_request
)
app.before_request(before_request)
app.after_request(after_request)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.api.v1.vendors import vendor_bp

app.register_blueprint(
    vendor_bp,
    url_prefix="/api/v1/vendors"
)
from app.api.v1.subscriptions import subscription_bp

app.register_blueprint(
    subscription_bp,
    url_prefix="/api/v1/subscriptions"
)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

limiter.init_app(app)
def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    # register blueprints

app.register_blueprint(billing_bp, url_prefix="/api/v1/billing")
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(tools_bp, url_prefix="/api/v1/tools")

    return app

from app.api.v1.payments import payment_bp

app.register_blueprint(payment_bp, url_prefix="/api/v1/pay")
