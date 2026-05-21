from flask import Flask
from config.base import Config

from app.extensions import db, jwt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.middleware.logger import before_request, after_request

from app.api.v1.tasks import tasks_bp
from app.api.v1.vendors import vendor_bp
from app.api.v1.subscriptions import subscription_bp
from app.api.v1.payouts import payout_bp
from app.api.v1.payments import payment_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # extensions
    db.init_app(app)
    jwt.init_app(app)

    # middleware
    app.before_request(before_request)
    app.after_request(after_request)

    # rate limiter
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["100 per hour"]
    )
    limiter.init_app(app)

    # blueprints
    app.register_blueprint(tasks_bp, url_prefix="/api/v1/tasks")
    app.register_blueprint(subscription_bp, url_prefix="/api/v1/subscriptions")
    app.register_blueprint(vendor_bp, url_prefix="/api/v1/vendors")
    app.register_blueprint(payout_bp, url_prefix="/api/v1/payouts")
    app.register_blueprint(payment_bp, url_prefix="/api/v1/payments")

    return app
