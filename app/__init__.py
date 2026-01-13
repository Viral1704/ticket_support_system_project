from flask import Flask

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()

def create_app(config_file = 'settings.py'):

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    migrate.init_app(app, db)

    from app import models

    from app.auth import auth

    app.register_blueprint(auth, url_prefix = '/auth')

    return app