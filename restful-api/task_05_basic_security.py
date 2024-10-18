#!/usr/bin/python3
"""
Module that def a function

"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
import jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SuperSecretKey'

users = {
      "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
      }


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_prot():
    return "Basic Auth: Access Granted", 200

@app.route("/login", methods=["POST"])
def login():
    r = request.get_json()
    user = users.get(r.get('username'))

    if not user or not check_password_hash(user['password'], r.get('password')):
        return {"error": "Invalid credentials"}, 401
    payload = {'username': user['username'], 'role': user['role']}
    token = create_access_token(identity=payload)
    return jsonify({"access_token": token}), 200


@app.route("/jwt-protected")
@jwt_required()
def prot():
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return "Admin Access: Granted", 200
    else:
        return "error: Admin access required", 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
