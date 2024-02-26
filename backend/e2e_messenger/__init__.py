from flask import Flask, send_file, send_from_directory, request
from flask_cors import CORS

from config import LocalConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    app.app_context().push()
    from e2e_messenger.extensions import api, db, celery_app, cache

    db.init_app(app)
    CORS(
        app,
        origins="http://localhost:5173",
    )
    celery_app.conf.update(app.config)
    cache.init_app(
        app,
        config={
            "CACHE_TYPE": "redis",
            "CACHE_REDIS_URL": "redis://localhost:6379/1",
            "prefix": "cache_",
        },
    )

    from e2e_messenger.controllers import auth_blueprint

    app.register_blueprint(auth_blueprint)

    from e2e_messenger.resources.user import UserResource, UsersResource
    from e2e_messenger.resources.message import MessageResource, MessagesResource
    from e2e_messenger.resources.role import RoleResource, RolesResource
    from e2e_messenger.resources.user_role import UserRoleResource, UserRolesResource
    from e2e_messenger.resources.access import AccessResource, AccessesResource
    from e2e_messenger.resources.report import ReportsResource

    api.add_resource(UserResource, "/user/<int:user_id>")
    api.add_resource(UsersResource, "/users")
    api.add_resource(MessageResource, "/message/<int:message_id>")
    api.add_resource(MessagesResource, "/messages")
    api.add_resource(RoleResource, "/role/<int:role_id>")
    api.add_resource(RolesResource, "/roles")
    api.add_resource(UserRoleResource, "/user/role/<int:user_role_id>")
    api.add_resource(UserRolesResource, "/user/roles")
    api.add_resource(AccessResource, "/access/<int:access_id>")
    api.add_resource(AccessesResource, "/accesses")
    api.add_resource(ReportsResource, "/reports")

    api.init_app(app)

    @app.route("/api/v1/status")
    def index():
        return {"status": "ok"}

    @app.route("/music/<int:music_id>")
    def music(music_id):
        return send_from_directory(
            "/home/krishnan/projects/mad-2-project-sessions/backend/e2e_messenger/music",
            "1.mp3",
        )

    @app.route("/add/<int:x>/<int:y>")
    def add(x, y):
        from .tasks import add

        result = add.delay(x, y)
        return {"task_id": result.id}

    @app.route("/task/<task_id>")
    def task(task_id):
        from .tasks import celery_app

        task = celery_app.AsyncResult(task_id)
        return {"status": task.status, "result": task.result}

    return app
