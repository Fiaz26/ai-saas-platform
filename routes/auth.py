from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    email = data["email"]
    password = generate_password_hash(data["password"])

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "user_id": user.id,
        "role": user.role
    })

    return jsonify({"token": token})
