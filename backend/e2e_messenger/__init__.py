from flask import Flask
from flask_cors import CORS

from config import LocalConfig

from e2e_messenger.extensions import api, db


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    app.app_context().push()
    db.init_app(app)
    CORS(
        app,
        origins="http://localhost:5173",
    )

    from e2e_messenger.controllers import auth_blueprint

    app.register_blueprint(auth_blueprint)

    from e2e_messenger.resources.user import UserResource, UsersResource
    from e2e_messenger.resources.message import MessageResource, MessagesResource
    from e2e_messenger.resources.role import RoleResource, RolesResource
    from e2e_messenger.resources.user_role import UserRoleResource, UserRolesResource
    from e2e_messenger.resources.access import AccessResource, AccessesResource

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

    api.init_app(app)

    @app.route("/api/v1/status")
    def index():
        return {"status": "ok"}

    return app
