from flask import Blueprint, jsonify, request

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    print(request.json)
    return jsonify({"message": "Tag created"}), 200
