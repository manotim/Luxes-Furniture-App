from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    _tablename_ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    hero_powers = db.relationship('HeroPower', backref='hero')

    
class Power(db.Model):
    _tablename_ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    hero_powers = db.relationship('HeroPower', backref='power')


class HeroPower(db.Model):
    _tablename_ = 'hero_power'

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), primary_key=True)
    strength = db.Column(db.String(255))