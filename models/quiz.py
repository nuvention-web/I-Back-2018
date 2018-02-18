from db import db
from datetime import datetime, timedelta

class QuizModel(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    ans1 = db.Column(db.Integer)
    ans2 = db.Column(db.Integer)
    ans3 = db.Column(db.Integer)
    ans4 = db.Column(db.Integer)
    time_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, ans1, ans2, ans3, ans4):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

