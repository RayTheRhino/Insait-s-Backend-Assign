from flask import Flask
from .models import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

migrate = Migrate()

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    return app
