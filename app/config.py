from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("postgresql://neondb_owner:npg_OPm5ADY7ZcfV@ep-quiet-frost-aoq7my5z-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require   ")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
