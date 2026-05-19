from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.payout_request import PayoutRequest
from app.models.vendor_wallet import VendorWallet

payout_bp = Blueprint("payouts", __name__)

@payout_bp.route("/request", methods=["POST"])
@jwt_required()
def request_payout():

    data = request.json

    vendor_id = data["vendor_id"]
    amount = float(data["amount"])

    wallet = VendorWallet.query.filter_by(
        vendor_id=vendor_id
    ).first()

    if not wallet:
        return {"error": "Wallet not found"}, 404

    if wallet.balance < amount:
        return {
            "error": "Insufficient balance"
        }, 400

    payout = PayoutRequest(
        vendor_id=vendor_id,
        amount=amount,
        method=data["method"],
        account_number=data["account_number"]
    )

    wallet.balance -= amount
    wallet.pending_balance += amount

    db.session.add(payout)
    db.session.commit()

    return jsonify({
        "message": "Payout request submitted"
    })
