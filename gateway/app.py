from flask import Flask
from config import Config
from extensions import db, jwt

from models.user import User
from models.tool import Tool
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()
