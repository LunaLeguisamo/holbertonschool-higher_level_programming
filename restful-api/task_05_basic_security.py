#!/usr/bin/python3
"""
Module that def a function

"""


from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
      "user1": {"username": "user1", "password": generate_password_hash("123"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("678"), "role": "admin"}
      }

@app.route("/data", methods=["POST", "GET"])
def verify(username, password):
    if username in users and check_password_hash(users['password'], password):
        return users['username']
    
@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    username = users.get('username')
    rol = users.get('rol')
    payload = {'usesrname': username, 'rol': rol}
    secretKey = 'SuperSecretKey'
    token = jwt.sign(payload, secretKey)
    return token

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_prot():        
    return "Basic Auth: Access Granted"

@app.route("/jwt-protected")
@jwt_required()
def prot():
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
def admin():
    if users['role'] == 'admin':
        return "Admin Access: Granted"
