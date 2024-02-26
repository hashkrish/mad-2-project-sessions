class LocalConfig:
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    JWT_SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/db.sqlite3"
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
    # CELERY_RESULT_BACKEND = "sqlite:///../instance/celery.sqlite3"
