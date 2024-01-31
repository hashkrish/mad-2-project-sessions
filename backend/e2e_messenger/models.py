from flask_login import UserMixin
from sqlalchemy import Integer, ForeignKey, String, Column, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship, backref

from e2e_messenger.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(128), index=True, unique=True)
    password = Column(String(128))
    active = Column(Boolean(), default=True)

    def check_password(self, password):
        return password == self.password

    @property
    def is_admin(self):
        admin_role = Role.query.filter_by(name="admin").first()
        return UserRole.query.filter_by(user_id=self.id, role_id=admin_role.id).first() is not None

    def __repr__(self):
        return "<User {}>".format(self.username)


class Role(db.Model):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    description = Column(String(128))

    def __repr__(self):
        return "<Role {}>".format(self.name)


class Access(db.Model):
    __tablename__ = "access"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    role_id = Column(Integer(), ForeignKey("role.id"), index=True)
    resource = Column(String(64))
    action = Column(String(64))

    def __repr__(self):
        return "<Access {}:{}:{}>".format(self.role_id, self.resource, self.action)


class UserRole(db.Model):
    __tablename__ = "user_role"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey("user.id"))
    role_id = Column(Integer(), ForeignKey("role.id"))

    def __repr__(self):
        return "<UserRole {}:{}>".format(self.user_id, self.role_id)


class Message(db.Model):
    __tablename__ = "message"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    sender_id = Column(Integer(), ForeignKey("user.id"), index=True)
    receiver_id = Column(Integer(), ForeignKey("user.id"), index=True)
    text = Column(String(256))
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

    def __repr__(self):
        return "<Message {}:{}>".format(self.sender_id, self.receiver_id)

"""
SQL to get the messages sent by user 1 to user 2:
SELECT * FROM message WHERE sender_id = 1 AND receiver_id = 2;

In sqlalchemy:
Message.query.filter_by(sender_id=1, receiver_id=2).all()

SQL to get to validate the access of user 1 to the messages sent by user 2:
SELECT * FROM access WHERE role_id IN (SELECT role_id FROM user_role WHERE user_id = 1)
    AND resource = 'message' AND action = 'read';

In sqlalchemy:
Access.query.filter(Access.role_id.in_(UserRole.query.filter_by(user_id=1).all()),
                    Access.resource == 'message',
                    Access.action == 'read').all()

Aggregate total messages sent by user 1:
SELECT COUNT(*) FROM message WHERE sender_id = 1;

In sqlalchemy:
Message.query.filter_by(sender_id=1).count()
"""
