from dotenv import load_dotenv
import os

load_dotenv()

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "postgresql://neondb_owner:npg_OPm5ADY7ZcfV@ep-quiet-frost-aoq7my5z-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require",
        "sqlite:///app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    
JAZZCASH_MERCHANT_ID = "YOUR_MERCHANT_ID"
JAZZCASH_INTEGRITY_SALT = "YOUR_SALT"
JAZZCASH_RETURN_URL = "https://yourdomain.com/api/v1/pay/jazzcash/callback"
