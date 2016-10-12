# Import the db from app
from __init__ import db

#TABLE EastZodiac
class EastZodiac(db.Model):
    __tablename__ = 'EastZodiac'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(200))

    def __repr__(self):
        return '<EastZodiac %r>' % self.name

#TABLE WestZodiac
class WestZodiac(db.Model):
    __tablename__ = 'WestZodiac'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(200))

    def __repr__(self):
        return '<WestZodiac %r>' % self.name
