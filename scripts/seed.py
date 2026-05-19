from app import create_app
from extensions import db
from models.tool import Tool
app = create_app()
from extensions import db
from models.tool import Tool
with app.app_context():

    tool = Tool(
        name="AI Writer",
        category="Content",
        url="https://chat.openai.com"
    )

    db.session.add(tool)
    db.session.commit()

    print("Seeded")
