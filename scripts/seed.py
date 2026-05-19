from app import create_app
from extensions import db
from models.tool import Tool

app = create_app()

with app.app_context():

    if Tool.query.first():
        print("Already seeded")
    else:
        tools = [
            Tool(name="AI Writer", category="Content", url="https://chat.openai.com"),
            Tool(name="SEO Tool", category="SEO", url="https://example.com")
        ]

        db.session.add_all(tools)
        db.session.commit()

        print("Database seeded successfully")
