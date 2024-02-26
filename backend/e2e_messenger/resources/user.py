from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError
from e2e_messenger.controllers import token_required

from e2e_messenger.extensions import db, cache
from e2e_messenger.models import User

from pickle import dumps, loads

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True)
parser.add_argument("email", type=str, required=True)
parser.add_argument("password", type=str, required=True)
parser.add_argument("active", type=bool, default=True)

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "active": fields.Boolean,
}


def abort_if_user_doesnt_exist(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {"error": "User {} doesn't exist".format(user_id)})


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = cache.get("user:{}".format(user_id))
        if user:
            print("Fetching user from cache")
            return loads(user), 200
        abort_if_user_doesnt_exist(user_id)
        user = User.query.filter_by(id=user_id).first()
        print("Fetching user from database")
        cache.set("user:{}".format(user_id), dumps(user))
        return user, 200

    @marshal_with(user_fields)
    def put(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        args = parser.parse_args()
        user = User.query.filter_by(id=user_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(user, arg, args[arg])
        db.session.commit()
        return user, 200

    @marshal_with(user_fields)
    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return user, 200


class UsersResource(Resource):
    @token_required
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users, 200

    @token_required
    @marshal_with(user_fields)
    def post(self):
        args = parser.parse_args()
        user = User(**args)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(409, "User already exists")
        return user, 201
