from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import bp

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(bp)
    CORS(app)

    return app