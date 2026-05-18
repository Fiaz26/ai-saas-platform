from flask import Blueprint, jsonify
from app.models.payment import Payment

admin_bp = Blueprint("admin", __name__, url_prefix="/api/v1/admin")


@admin_bp.route("/payments", methods=["GET"])
def get_payments():

    payments = Payment.query.filter_by(status="pending").all()

    return jsonify([
        {
            "id": p.id,
            "user_id": p.user_id,
            "amount": p.amount,
            "method": p.method,
            "transaction_id": p.transaction_id
        }
        for p in payments
    ])


@admin_bp.route("/reject/<int:payment_id>", methods=["POST"])
def reject(payment_id):

    payment = Payment.query.get(payment_id)
    payment.status = "rejected"

    from app.extensions import db
    db.session.commit()

    return jsonify({"message": "Rejected"})
