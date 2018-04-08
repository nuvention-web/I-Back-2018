from db import db
from models.scent_profile import ScentProfileModel
from datetime import datetime, timedelta

class PerfumeModel(db.Model):
    __tablename__ = 'perfume'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(200))
    designer = db.Column(db.String(200))
    image_lnk = db.Column(db.String(248))
    buy_lnk = db.Column(db.String(248))
    scent_profile_id = db.Column(db.Integer, db.ForeignKey(ScentProfileModel.id))

    def __init__(self, name, designer, image_lnk, buy_lnk, scent_profile_id):
        self.name = name 
        self.designer = designer 
        self.image_lnk = image_lnk
        self.buy_lnk = buy_lnk
        self.scent_profile_id = scent_profile_id
    
    def json_debug(self):
        return {'id': self.id, 'name': self.name, 'designer': self.designer, 'image_lnk': self.image_lnk, 'buy_lnk': self.buy_lnk, 'scent_profile_id': self.scent_profile_id}

    def json(self):
        return {'id': self.id, 'name': self.name, 'designer': self.designer, 'image_lnk': self.image_lnk, 'buy_lnk': self.buy_lnk}

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
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_designer(cls, designer):
        return cls.query.filter_by(designer=designer).all()

    @classmethod
    def filter_by_scent_profile_id(cls, scent_profile_id):
        return cls.query.filter_by(scent_profile_id=scent_profile_id).all()

