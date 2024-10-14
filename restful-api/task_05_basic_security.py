#!/usr/bin/python3
"""
Module that def a function

"""


from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {
      "user1": {"username": "user1", "password": generate_password_hash("123"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("678"), "role": "admin"}
      }

@app.route("/data", methods=["POST", "GET"])
def verify(username, password):
    if username in users and check_password_hash(users['password'], password):
        return users['username']
