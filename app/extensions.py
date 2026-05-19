from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from redis import Redis

db = SQLAlchemy()
jwt = JWTManager()

redis_client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)
