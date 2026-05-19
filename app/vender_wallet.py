from app.extensions import db

class VendorWallet(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    vendor_id = db.Column(
        db.Integer,
        unique=True
    )

    balance = db.Column(
        db.Float,
        default=0
    )

    pending_balance = db.Column(
        db.Float,
        default=0
    )

    lifetime_earnings = db.Column(
        db.Float,
        default=0
    )
from flask import Blueprint, jsonify

from app.models.vendor_wallet import VendorWallet

wallet_bp = Blueprint("wallet", __name__)

@wallet_bp.route("/<int:vendor_id>")
def get_wallet(vendor_id):

    wallet = VendorWallet.query.filter_by(
        vendor_id=vendor_id
    ).first()

    if not wallet:
        return {"error": "Wallet not found"}, 404

    return jsonify({
        "balance": wallet.balance,
        "pending_balance": wallet.pending_balance,
        "lifetime_earnings": wallet.lifetime_earnings
    })
