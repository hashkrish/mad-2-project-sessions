from datetime import datetime, timedelta
from functools import wraps

from config import LocalConfig
from flask import Blueprint, jsonify, request
from jwt import decode, encode

from e2e_messenger.extensions import db
from e2e_messenger.models import User
from e2e_messenger.validation import Validator


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify(
                {
                    "message": {"error": "token missing"},
                }
            )

        jwt_data = None
        try:
            jwt_data = decode(
                token,
                LocalConfig.JWT_SECRET_KEY,
                algorithms=["HS256"],
            )
        except:
            return jsonify(
                {
                    "message": {"error": {"message": "Invalid token"}},
                }
            )
        return f(*args, **kwargs)

    return decorator


auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return (
            jsonify({"message": {"error": "User {} doesn't exist".format(username)}}),
            400,
        )
    if not user.check_password(password):
        return jsonify({"message": {"error": "Wrong password"}}), 400
    jwt = encode(
        {"username": username, "exp": datetime.now() + timedelta(minutes=30)},
        LocalConfig.JWT_SECRET_KEY,
        algorithm="HS256",
    )
    return (
        jsonify(
            {
                "status": "ok",
                "jwt": jwt,
            }
        ),
        200,
    )
