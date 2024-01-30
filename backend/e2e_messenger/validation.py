import re
from e2e_messenger.models import User, Message, Role

class Validator:
    @staticmethod
    def user_id_validator(user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise ValueError("User {} doesn't exist".format(user_id))
        return user.id

    @staticmethod
    def message_id_validator(message_id):
        message = Message.query.filter_by(id=message_id).first()
        if not message:
            raise ValueError("Message {} doesn't exist".format(message_id))
        return message.id

    @staticmethod
    def role_id_validator(role_id):
        role = Role.query.filter_by(id=role_id).first()
        if not role:
            raise ValueError("Role {} doesn't exist".format(role_id))
        return role.id

    @staticmethod
    def action_validator(action):
        if action not in ["create", "read", "update", "delete", "list"]:
            raise ValueError("Action {} is not supported".format(action))
        return action

    @staticmethod
    def regex_validator(regex):
        try:
            re.compile(regex)
        except re.error:
            raise ValueError("Regex {} is not valid".format(regex))
        return regex
