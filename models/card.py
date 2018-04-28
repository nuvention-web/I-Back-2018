from db import db
from datetime import datetime, timedelta

class CardModel(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(100))
    accord = db.Column(db.String(100))
    image_lnk = db.Column(db.String(2000))
    vid_lnk = db.Column(db.String(2000))
    start_time = db.Column(db.Integer)
    description = db.Column(db.String(1000))

    def __init__(self, name, accord, image_lnk, vid_lnk, start_time, description):
        self.name = name
        self.accord = accord 
        self.image_lnk = image_lnk
        self.vid_lnk = vid_lnk
        self.start_time = start_time
        self.description = description

    def json(self):
        return {
                    "name": self.name,
                    "accord": self.accord,
                    "image_lnk": self.image_lnk,
                    "vid_lnk": self.vid_lnk,
                    "start_time": self.start_time,
                    "description": self.description,
               }
        
    def json_debug(self):
        return {
                    "id": self.id
                    "name": self.name,
                    "accord": self.accord,
                    "image_lnk": self.image_lnk,
                    "vid_lnk": self.vid_lnk,
                    "start_time": self.start_time,
                    "description": self.description,
               }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def filter_by_accord(cls, accord):
        return cls.query.filter(accord=accord).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

