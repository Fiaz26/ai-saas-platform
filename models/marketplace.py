from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.models.ai_api import AIAPI

marketplace_bp = Blueprint(
    "marketplace",
    __name__
)

@marketplace_bp.route("/")
@jwt_required()
def list_marketplace():

    apis = AIAPI.query.filter_by(active=True).all()

    return jsonify([
        {
            "name": api.name,
            "slug": api.slug,
            "category": api.category,
            "description": api.description,
            "credit_cost": api.credit_cost
        }
        for api in apis
    ])
