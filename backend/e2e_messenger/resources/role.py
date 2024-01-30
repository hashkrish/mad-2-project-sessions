from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError
from e2e_messenger.controllers import token_required

from e2e_messenger.extensions import db
from e2e_messenger.models import Role

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True)
parser.add_argument("description", type=str, required=False)

role_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
}

def abort_if_role_doesnt_exist(role_id):
    role = Role.query.filter_by(id=role_id).first()
    if not role:
        abort(404, {"error": "Role {} doesn't exist".format(role_id)})

class RoleResource(Resource):
    @token_required
    @marshal_with(role_fields)
    def get(self, role_id):
        abort_if_role_doesnt_exist(role_id)
        role = Role.query.filter_by(id=role_id).first()
        return role, 200

    @token_required
    @marshal_with(role_fields)
    def put(self, role_id):
        abort_if_role_doesnt_exist(role_id)
        args = parser.parse_args()
        role = Role.query.filter_by(id=role_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(role, arg, args[arg])
        db.session.commit()
        return role, 200

    @token_required
    @marshal_with(role_fields)
    def delete(self, role_id):
        abort_if_role_doesnt_exist(role_id)
        role = Role.query.filter_by(id=role_id).first()
        db.session.delete(role)
        db.session.commit()
        return role, 200

class RolesResource(Resource):
    @token_required
    @marshal_with(role_fields)
    def get(self):
        roles = Role.query.all()
        return roles, 200

    @token_required
    @marshal_with(role_fields)
    def post(self):
        args = parser.parse_args()
        role = Role(**args)
        try:
            db.session.add(role)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(409, {"error": "Role {} already exists".format(role.name)})
        return role, 201
