
from flask import Blueprint, jsonify
from controllers.stream_controller import fetch_streams

stream_bp = Blueprint('stream', __name__)

@stream_bp.route("/streams", methods=["GET"])
def get_streams():
    data = fetch_streams()
    return jsonify(data)