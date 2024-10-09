from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class AskRecord(db.Model):
    __tablename__ = 'ask_records'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text)
    error = db.Column(db.Text)
    status_code = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, question, response=None, error=None, status_code=None):
        self.question = question
        self.response = response
        self.error = error
        self.status_code = status_code