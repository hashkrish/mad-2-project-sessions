from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from celery import Celery
from flask_caching import Cache

cache = Cache()

api = Api(prefix="/api/v1")


class Base(DeclarativeBase):
    __abstract__ = True


db = SQLAlchemy(model_class=Base)
celery_app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    # backend="sqlite:///instance/celery.sqlite3",
    backend="redis://127.0.0.1:6379/0",
)
