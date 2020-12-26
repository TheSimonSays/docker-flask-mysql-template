from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.cli import bp as cli_bp
    app.register_blueprint(cli_bp)

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
