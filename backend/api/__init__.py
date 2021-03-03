from backend.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from backend.api.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/api")

    return app