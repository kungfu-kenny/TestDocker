from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from web.app import app


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, date) -> None:
        self.date = date

    def __repr__(self) -> str:
        return f"{self.id}, {self.date}"

db.create_all()