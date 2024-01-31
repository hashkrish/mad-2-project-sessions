import re
from datetime import datetime, timedelta
from functools import wraps

from config import LocalConfig
from flask import Blueprint, jsonify, request
from jwt import decode, encode

from e2e_messenger.extensions import db
from e2e_messenger.models import Access, User, UserRole
from e2e_messenger.validation import Validator

method_to_action = {
    "POST": "create",
    "GET": "read",
    "PUT": "update",
    "DELETE": "delete",
}


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
            user = User.query.filter_by(username=jwt_data["username"]).first()
            if not user:
                return jsonify(
                    {"message": {"error": f"User {jwt_data['username']} doesn't exist"}}
                )

            if jwt_data["exp"] < datetime.now():
                return jsonify({"message": {"error": "Token expired"}})

            if user.is_admin:
                return f(*args, **kwargs)

            user_roles = UserRole.query.filter_by(user_id=user.id).all()
            accessess = []
            for user_role in user_roles:
                role_accessess = (
                    Access.query.filter_by(role_id=user_role.role_id)
                    .where(Access.action == method_to_action[request.method])
                    .all()
                )
                accessess.extend([access.resource for access in role_accessess])

            for regex in accessess:
                if re.match(regex, request.path):
                    return f(*args, **kwargs)
            return jsonify(
                {
                    "message": {
                        "error": f"User {jwt_data['username']} doesn't have access to {request.method} {request.path}"
                    }
                }
            )

        except:
            return jsonify({"message": {"error": "Invalid token"}})

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
