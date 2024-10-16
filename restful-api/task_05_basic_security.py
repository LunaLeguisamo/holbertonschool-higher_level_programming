#!/usr/bin/python3
"""
Module that def a function

"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
#jwt = JWTManager(app)

users = {
      "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
      }
    
secretKey = '10'
@app.route("/login", methods=["POST"])
def login():
    r = request.get_json()
    for i in users:
        if users[i]['username'] == r.get('username'):
            user = users[i]
            break
    else:
        return "not found", 404
    if not check_password_hash(user['password'], r.get('password')):
        return "wrong password", 403
    username = user.get('username')
    role = user.get('role')
    payload = {'username': username, 'role': role}
    token = jwt.encode(payload, secretKey)
    return token

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_prot():        
    return "Basic Auth: Access Granted"

@app.route("/jwt-protected")
@jwt_required()
def prot():
    get_jwt_identity()
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin():
    get_jwt_identity()
    if users['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(debug=True)
