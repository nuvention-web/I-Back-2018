from db import db
from datetime import datetime, timedelta

class ScentProfileModel(db.Model):
    __tablename__ = 'scent_profile'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    tag1 = db.Column(db.String(100))
    tag2 = db.Column(db.String(100))
    sillage = db.Column(db.String(20))
    image_lnk = db.Column(db.String(248))
    sound_lnk = db.Column(db.String(248))
    children = db.relationship("PerfumeModel")

    def __init__(self, q6, q7, tag1, tag2, sillage, image_lnk, sound_lnk):
        self.q6 = q6
        self.q7 = q7
        self.tag1 = tag1
        self.tag2 = tag2
        self.sillage = sillage
        self.image_lnk = image_lnk
        self.sound_lnk = sound_lnk

    def json(self):
        return {'id': self.id, 'q6': self.q6, 'q7': self.q7, 'tag1': self.tag1, 'tag2': self.tag2, 'sillage': self.sillage, 'image_lnk': self.image_lnk, 'sound_lnk': self.sound_lnk}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_qs(cls, q6, q7):
        return cls.query.filter_by(q6=q6, q7=q7).first()

    @classmethod
    def find_by_q6(cls, q6):
        return cls.query.filter_by(q6=q6).all()

    @classmethod
    def find_by_q7(cls, q7):
        return cls.query.filter_by(q7=q7).all()

    @classmethod
    def filter_by_sillage(cls, sillage):
        return cls.query.filter_by(sillage=sillage).all()

    @classmethod
    def filter_by_tag1(cls, tag1):
        return cls.query.filter_by(tag1=tag1).all()

    @classmethod
    def filter_by_tag2(cls, tag2):
        return cls.query.filter_by(tag2=tag2).all()

    @classmethod
    def find_by_tags(cls, tag1, tag2):
        return cls.query.filter_by(tag1=tag1).filter_by(tag2=tag2).first()
    
