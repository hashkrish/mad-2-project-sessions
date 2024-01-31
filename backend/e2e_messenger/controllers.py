import re
from datetime import datetime, timedelta
from functools import wraps

from werkzeug.exceptions import BadRequest, NotFound

from config import LocalConfig
from flask import Blueprint, jsonify, request, make_response
from jwt import ExpiredSignatureError, decode, encode

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
            return make_response(
                {
                    "message": {"error": "token missing"},
                },
                401,
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
                return make_response(
                    {
                        "message": {
                            "error": f"User {jwt_data['username']} doesn't exist"
                        }
                    },
                    404,
                )

            token_exp = datetime.utcfromtimestamp(jwt_data["exp"])
            current_time = datetime.utcnow()
            if token_exp < current_time:
                return make_response({"message": {"error": "Token expired"}}, 401)

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
                    print(f"Success with {regex}")
                    return f(*args, **kwargs)
                else:
                    print(f"Failed with {regex}")

            return make_response(
                {
                    "message": {
                        "error": f"User {jwt_data['username']} doesn't have access to {request.method} {request.path}"
                    }
                },
                403,
            )

        except BadRequest:
            return make_response({"message": {"error": "Bad Request"}}, 400)
        except NotFound:
            return make_response({"message": {"error": "Not Found"}}, 404)
        except ExpiredSignatureError:
            return make_response({"message": {"error": "Signature has expired"}}, 401)
        except Exception as e:
            # TODO: This is a catch-all exception handler. It should be removed in production
            return make_response({"message": {"error": str(e)}}, 401)

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
        {"username": username, "exp": datetime.utcnow() + timedelta(minutes=30)},
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
