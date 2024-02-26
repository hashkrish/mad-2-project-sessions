from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    # backend="sqlite:///instance/celery.sqlite3",
    backend="redis://127.0.0.1:6379/0",
)
