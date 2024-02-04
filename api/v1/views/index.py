#!/usr/bin/python3
"""Module index.py"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """Returns API status"""
    return jsonify({"status": "OK"})
