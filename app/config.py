import os

class Config:
    SECRET_KEY = "super-secret"

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://neondb_owner:npg_OPm5ADY7ZcfV@ep-quiet-frost-aoq7my5z-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require "
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt-secret"
