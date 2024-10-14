#!/usr/bin/python3
"""
Module that def a function

"""


from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash