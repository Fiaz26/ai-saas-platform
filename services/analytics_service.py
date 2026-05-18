from app.models.user import User
from app.models.payment import Payment
from app.models.usage import Usage

def get_dashboard_stats():

    return {
        "users": User.query.count(),
        "revenue": sum(p.amount for p in Payment.query.filter_by(status="approved")),
        "usage": Usage.query.count()
    }
