from flask import Blueprint, jsonify

from app.extensions import db

from app.models.payout_request import PayoutRequest
from app.models.vendor_wallet import VendorWallet

admin_payout_bp = Blueprint(
    "admin_payouts",
    __name__
)

@admin_payout_bp.route("/approve/<int:payout_id>")
def approve_payout(payout_id):

    payout = PayoutRequest.query.get(payout_id)

    if not payout:
        return {"error": "Not found"}, 404

    payout.status = "paid"

    wallet = VendorWallet.query.filter_by(
        vendor_id=payout.vendor_id
    ).first()

    wallet.pending_balance -= payout.amount

    db.session.commit()

    return jsonify({
        "message": "Payout approved"
    })
