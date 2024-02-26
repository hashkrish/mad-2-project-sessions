from e2e_messenger import create_app

app = create_app()
with app.app_context():
    from e2e_messenger.extensions import db

    db.create_all()
