from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if email == "admin@test.com" and password == "1234":

        token = create_access_token(identity={
            "email": email,
            "role": "admin"
        })

        return jsonify({
            "token": token
        })

    return jsonify({"error": "Invalid credentials"}), 401
