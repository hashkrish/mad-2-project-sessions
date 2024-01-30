from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError
from e2e_messenger.controllers import token_required

from e2e_messenger.extensions import db
from e2e_messenger.models import Access
from e2e_messenger.validation import Validator

parser = reqparse.RequestParser()
parser.add_argument("role_id", type=Validator.role_id_validator, required=True)
parser.add_argument("resource", type=Validator.regex_validator, required=True)
parser.add_argument("action", type=Validator.action_validator, required=True)

access_fields = {
    "id": fields.Integer,
    "role_id": fields.Integer,
    "resource": fields.String,
    "action": fields.String,
}


def abort_if_access_doesnt_exist(access_id):
    access = Access.query.filter_by(id=access_id).first()
    if not access:
        abort(404, {"error": "Access {} doesn't exist".format(access_id)})
    return access


class AccessResource(Resource):
    @token_required
    @marshal_with(access_fields)
    def get(self, access_id):
        abort_if_access_doesnt_exist(access_id)
        access = Access.query.filter_by(id=access_id).first()
        return access, 200

    @token_required
    @marshal_with(access_fields)
    def put(self, access_id):
        abort_if_access_doesnt_exist(access_id)
        args = parser.parse_args()
        access = Access.query.filter_by(id=access_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(access, arg, args[arg])
        db.session.commit()
        return access, 200

    @token_required
    @marshal_with(access_fields)
    def delete(self, access_id):
        abort_if_access_doesnt_exist(access_id)
        access = Access.query.filter_by(id=access_id).first()
        db.session.delete(access)
        db.session.commit()
        return access, 200


class AccessesResource(Resource):
    @token_required
    @marshal_with(access_fields)
    def get(self):
        accesses = Access.query.all()
        return accesses, 200

    @token_required
    @marshal_with(access_fields)
    def post(self):
        args = parser.parse_args()
        access = Access(
            role_id=args["role_id"],
            resource=args["resource"],
            action=args["action"],
        )
        db.session.add(access)
        db.session.commit()
        return access, 201
