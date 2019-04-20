import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')

app_version = "0.1.0-test.6"

@app.route("/version", methods=["GET"])
def version():
    return jsonify({"version": app_version})

from app import validating_apis
