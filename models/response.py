from db import db
from models.perfume import PerfumeModel
from datetime import datetime

class ResponseModel(db.Model):
    __tablename__ = 'response'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    perfume_id = db.Column(db.Integer, db.ForeignKey(PerfumeModel.id))
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

    def __init__(self, perfume_id, q1, q2, q3, q4, q5):
        self.perfume_id = perfume_id
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
    
    def json(self):
        return {
            'id': self.id,
            'perfume_id': self.perfume_id,
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3,
            'q4': self.q4,
            'q5': self.q5,
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
    def filter_below_id(cls, _id):
        return cls.query.filter(cls.id <= _id).all()
    
    @classmethod
    def filter_by_q1(cls, q1):
        return cls.query.filter_by(q1=q1).all()
    
    @classmethod
    def filter_by_q2(cls, q2):
        return cls.query.filter_by(q2=q2).all()
    
    @classmethod
    def filter_by_q3(cls, q3):
        return cls.query.filter_by(q3=q3).all()
    
    @classmethod
    def filter_by_q4(cls, q4):
        return cls.query.filter_by(q4=q4).all()
    
    @classmethod
    def filter_by_q5(cls, q5):
        return cls.query.filter_by(q5=q5).all()
