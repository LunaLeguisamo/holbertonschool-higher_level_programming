#!/usr/bin/python3
"""
Module that def a function

"""

from flask import Flask, jsonify, request
app = Flask(__name__)

users_list = {
        "luna": {"username": "luna", "name": "Luna", "age": 26, "city": "Montevideo"},
        "owen": {"username": "owen", "name": "Owen", "age": 30, "city": "New York"}
        }
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users_list.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def users(username):
    username_ = users_list.get(username)
    if username_:
        return jsonify(username_)
    else:
        return jsonify({"error": "User not found"})
    
@app.route("/add_user", methods=["POST"])
def add():
    new_user = request.get_json()
    user = new_user['username']
    name = new_user['name']
    age = new_user['age']
    city = new_user['city']
    if not isinstance(user, str):
        return jsonify({"error": "User not found"})
    
    users_list[user] = {"username": user, "name": name, "age": age, "city": city}
    message = {"message": "User added", "user":users_list[user]}
    
    return jsonify(message)
    
if __name__ == "__main__":
    app.run()
