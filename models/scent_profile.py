from db import db
from datetime import datetime, timedelta

class ScentProfileModel(db.Model):
    __tablename__ = 'scent_profile'

    id = db.Column(db.Integer, primary_key=True)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    
