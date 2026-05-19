from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.payments.jazzcash import generate_jazzcash_payload

payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/jazzcash/init", methods=["POST"])
@jwt_required()
def init_payment():

    user_id = get_jwt_identity()
    amount = request.json.get("amount")
    

    order_id = f"ORDER_{user_id}"

    payload = generate_jazzcash_payload(amount, order_id)

    return jsonify({
        "payment_url": "https://sandbox.jazzcash.com.pk/CustomerPortal/transactionmanagement/merchantform/",
        "payload": payload
    })
from app.services.billing_service import BillingService

@payment_bp.route("/jazzcash/callback", methods=["POST"])
def jazzcash_callback():

    data = request.form

    status = data.get("pp_ResponseCode")
    user_id = data.get("pp_BillReference")

    if status == "000":

        SubscriptionService.create_subscription(
    user_id=payment.user_id,
    plan_name="pro"
)

        return "Payment Successful"

    return "Payment Failed"
