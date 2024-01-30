from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError
from e2e_messenger.controllers import token_required

from e2e_messenger.extensions import db
from e2e_messenger.models import UserRole
from e2e_messenger.validation import Validator

parser = reqparse.RequestParser()
parser.add_argument("user_id", type=Validator.user_id_validator, required=True)
parser.add_argument("role_id", type=Validator.role_id_validator, required=True)

user_role_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "role_id": fields.Integer,
}


def abort_if_user_role_doesnt_exist(user_role_id):
    user_role = UserRole.query.filter_by(id=user_role_id).first()
    if not user_role:
        abort(404, {"error": "UserRole {} doesn't exist".format(user_role_id)})
    return user_role


class UserRoleResource(Resource):
    @token_required
    @marshal_with(user_role_fields)
    def get(self, user_role_id):
        abort_if_user_role_doesnt_exist(user_role_id)
        user_role = UserRole.query.filter_by(id=user_role_id).first()
        return user_role, 200

    @token_required
    @marshal_with(user_role_fields)
    def put(self, user_role_id):
        abort_if_user_role_doesnt_exist(user_role_id)
        args = parser.parse_args()
        user_role = UserRole.query.filter_by(id=user_role_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(user_role, arg, args[arg])
        db.session.commit()
        return user_role, 200

    @token_required
    @marshal_with(user_role_fields)
    def delete(self, user_role_id):
        abort_if_user_role_doesnt_exist(user_role_id)
        user_role = UserRole.query.filter_by(id=user_role_id).first()
        db.session.delete(user_role)
        db.session.commit()
        return user_role, 200


class UserRolesResource(Resource):
    @token_required
    @marshal_with(user_role_fields)
    def get(self):
        user_roles = UserRole.query.all()
        return user_roles, 200

    @token_required
    @marshal_with(user_role_fields)
    def post(self):
        args = parser.parse_args()
        user_role = UserRole(**args)
        try:
            db.session.add(user_role)
            db.session.commit()
        except IntegrityError:
            abort(409, {"error": "UserRole already exists"})
        return user_role, 201
