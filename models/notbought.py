from db import db
from datetime import datetime, timedelta

class NotBoughtModel(db.Model):
    __tablename__ = 'notbought'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(100))
    q1 = db.Column(db.String(100))
    q2 = db.Column(db.String(100))
    q3 = db.Column(db.String(100))

    def __init__(self, name, q1, q2, q3):
        self.name = name
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def json(self):
        return {
                    "id": self.id,
                    "name": self.name,
                    "created": self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
                    "q1": self.q1,
                    "q2": self.q2,
                    "q3": self.q3,
               }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name == name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

