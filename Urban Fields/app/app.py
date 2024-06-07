from flask import Flask
from config import Config
from models import db
from routes import bp

def create_app():
    app = Flask(_name_)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(bp)

    return app