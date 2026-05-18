from flask import Blueprint, jsonify
from app.models.user import User
from app.models.payment import Payment
from app.models.usage import Usage

analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/v1/analytics")


@analytics_bp.route("/overview", methods=["GET"])
def overview():

    total_users = User.query.count()

    revenue = sum(
        p.amount for p in Payment.query.filter_by(status="approved").all()
    )

    pending_payments = Payment.query.filter_by(status="pending").count()

    total_usage = Usage.query.count() if Usage.query.first() else 0

    return jsonify({
        "total_users": total_users,
        "revenue": revenue,
        "pending_payments": pending_payments,
        "total_usage": total_usage
    })
