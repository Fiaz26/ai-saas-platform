I'mfrom app.extensions import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.String(120), unique=True)

    amount = db.Column(db.Integer)
    status = db.Column(db.String(50))  # success / failed / pending

    provider = db.Column(db.String(50))  # jazzcash

    txn_ref = db.Column(db.String(120))
    raw_response = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
import hashlib
from flask import request
from app.models.payment import Payment
from app.extensions import db
from app.services.billing_service import BillingService
from config import Config
@payment_bp.route("/jazzcash/callback", methods=["POST"])
def jazzcash_callback():

    data = request.form.to_dict()

    received_hash = data.get("pp_SecureHash", "")
    order_id = data.get("pp_BillReference")
    status = data.get("pp_ResponseCode")
    txn_ref = data.get("pp_TxnRefNo")

    # STEP 1 — remove secure hash from payload
    filtered = {k: v for k, v in data.items() if k != "pp_SecureHash"}

    sorted_string = "&".join([f"{k}={filtered[k]}" for k in sorted(filtered)])
    local_hash = hashlib.sha256(
        (Config.JAZZCASH_INTEGRITY_SALT + "&" + sorted_string).encode()
    ).hexdigest().upper()

    # STEP 2 — HASH VALIDATION (CRITICAL SECURITY)
    if local_hash != received_hash:
        return "Invalid Signature", 403

    # STEP 3 — FIND EXISTING PAYMENT (IDEMPOTENCY CHECK)
    existing = Payment.query.filter_by(order_id=order_id).first()

    if existing and existing.status == "success":
        return "Already processed", 200

    # STEP 4 — SAVE PAYMENT RECORD
    payment = Payment(
        user_id=int(order_id.replace("ORDER_", "")),
        order_id=order_id,
        amount=int(data.get("pp_Amount", 0)) // 100,
        status="success" if status == "000" else "failed",
        provider="jazzcash",
        txn_ref=txn_ref,
        raw_response=str(data)
    )

    db.session.add(payment)
    db.session.commit()

    # STEP 5 — ONLY CREDIT ON SUCCESS
    if status == "000":
        BillingService.add_credits(
            user_id=payment.user_id,
            amount=payment.amount,
            method="jazzcash"
        )

    return "OK", 200
    import uuid

order_id = f"JC_{user_id}_{uuid.uuid4().hex[:10]}"

@payment_bp.route("/status/<order_id>")
@jwt_required()
def payment_status(order_id):

    payment = Payment.query.filter_by(order_id=order_id).first()

    if not payment:
        return {"error": "Not found"}, 404

    return {
        "status": payment.status,
        "amount": payment.amount,
        "provider": payment.provider
    }
