from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db

billing_bp = Blueprint("billing", __name__, url_prefix="/api/v1/billing")


@billing_bp.route("/credits", methods=["GET"])
@jwt_required()
def get_credits():

    user_data = get_jwt_identity()
    user = User.query.get(user_data["user_id"])

    return jsonify({
        "credits": user.credits
    })


@billing_bp.route("/deduct", methods=["POST"])
@jwt_required()
def deduct_credits():

    user_data = get_jwt_identity()
    user = User.query.get(user_data["user_id"])

    user.credits -= 1

    db.session.commit()

    return jsonify({
        "credits": user.credits
    })
