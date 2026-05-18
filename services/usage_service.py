from app.models.usage import Usage
from app.extensions import db

def log_usage(user_id, tool_name, credits=1):

    usage = Usage(
        user_id=user_id,
        tool_name=tool_name,
        credits_used=credits
    )

    db.session.add(usage)
    db.session.commit()
