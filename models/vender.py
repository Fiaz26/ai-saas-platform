from app.extensions import db

class Vendor(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))

    email = db.Column(db.String(120), unique=True)

    company = db.Column(db.String(120))

    api_key = db.Column(db.String(255))

    active = db.Column(db.Boolean, default=True)
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.extensions import db
from app.models.ai_api import AIAPI

vendor_bp = Blueprint("vendors", __name__)

@vendor_bp.route("/upload-api", methods=["POST"])
@jwt_required()
def upload_api():

    data = request.json

    api = AIAPI(
        name=data["name"],
        slug=data["slug"],
        category=data["category"],
        description=data["description"],
        endpoint=data["endpoint"],
        credit_cost=data["credit_cost"],
        vendor_id=data["vendor_id"]
    )

    db.session.add(api)
    db.session.commit()

    return jsonify({
        "message": "API uploaded"
    })
