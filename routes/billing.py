from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.payment import Payment
from app.models.user import User
from app.extensions import db

billing_bp = Blueprint("billing", __name__, url_prefix="/api/v1/billing")


# USER SUBMITS PAYMENT PROOF
@billing_bp.route("/submit-payment", methods=["POST"])
@jwt_required()
def submit_payment():

    user_data = get_jwt_identity()

    data = request.get_json()

    payment = Payment(
        user_id=user_data["user_id"],
        amount=data["amount"],
        method=data["method"],
        transaction_id=data["transaction_id"],
        status="pending"
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({"message": "Payment submitted, awaiting approval"})


# ADMIN APPROVES PAYMENT
@billing_bp.route("/approve/<int:payment_id>", methods=["POST"])
def approve_payment(payment_id):

    payment = Payment.query.get(payment_id)
    payment.status = "approved"

    user = User.query.get(payment.user_id)

    # CREDIT ALLOCATION LOGIC
    user.credits += int(payment.amount * 10)

    db.session.commit()

    return jsonify({"message": "Payment approved"})
