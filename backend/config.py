class LocalConfig:
    FLASK_ENV = 'development'
    FLASK_DEBUG = True
    JWT_SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/db.sqlite3'
