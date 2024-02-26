from datetime import datetime
from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy.exc import IntegrityError
from e2e_messenger.controllers import token_required

from e2e_messenger.extensions import db
from e2e_messenger.models import Message
from e2e_messenger.validation import Validator

parser = reqparse.RequestParser()
parser.add_argument("sender_id", type=Validator.user_id_validator, required=True)
parser.add_argument("receiver_id", type=Validator.user_id_validator, required=True)
parser.add_argument("text", type=str, required=True)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument("sender_id", type=Validator.user_id_validator)
patch_parser.add_argument("receiver_id", type=Validator.user_id_validator)
patch_parser.add_argument("text", type=str)

message_fields = {
    "id": fields.Integer,
    "sender_id": fields.Integer,
    "receiver_id": fields.Integer,
    "text": fields.String,
    "timestamp": fields.String,
}


def abort_if_message_doesnt_exist(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if not message:
        abort(404, {"error": "Message {} doesn't exist".format(message_id)})


class MessageResource(Resource):
    @token_required
    @marshal_with(message_fields)
    def get(self, message_id):
        abort_if_message_doesnt_exist(message_id)
        message = Message.query.filter_by(id=message_id).first()
        return message, 200

    @token_required
    @marshal_with(message_fields)
    def put(self, message_id):
        abort_if_message_doesnt_exist(message_id)
        args = patch_parser.parse_args()
        message = Message.query.filter_by(id=message_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(message, arg, args[arg])
        db.session.commit()
        return message, 200

    @token_required
    @marshal_with(message_fields)
    def patch(self, message_id):
        abort_if_message_doesnt_exist(message_id)
        args = patch_parser.parse_args()
        message = Message.query.filter_by(id=message_id).first()
        for arg in args:
            if args[arg] is not None:
                setattr(message, arg, args[arg])
        db.session.commit()
        return message, 200

    @token_required
    @marshal_with(message_fields)
    def delete(self, message_id):
        abort_if_message_doesnt_exist(message_id)
        message = Message.query.filter_by(id=message_id).first()
        db.session.delete(message)
        db.session.commit()
        return message, 200


class MessagesResource(Resource):
    @token_required
    @marshal_with(message_fields)
    def get(self):
        messages = Message.query.paginate(error_out=False).items
        return messages, 200

    @token_required
    @marshal_with(message_fields)
    def post(self):
        args = parser.parse_args()
        message = Message(**args)
        try:
            db.session.add(message)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(409, {"error": "Message {} already exists".format(message.id)})
        return message, 201
