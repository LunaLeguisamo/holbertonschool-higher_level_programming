#!/usr/bin/python3
"""
Module that def a function

"""

from flask import Flask, jsonify, request
app = Flask(__name__)

users_list = {
        "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
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
        return {"error": "User not found"}

with app.add_request_context('/add_user', method='POST'):
    assert request.path == '/add_user'
    assert request.method == 'POST'
    
    @app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run()
