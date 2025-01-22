from . import db
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kommune = db.Column(db.String(100), nullable=False)
    bundesland = db.Column(db.String(100))
    low_income = db.Column(db.Float)
    general_funds = db.Column(db.Float)
    elderly_percentage = db.Column(db.Float)
    long_term_unemployment = db.Column(db.Float)
    debt = db.Column(db.Float)
    admin_type = db.Column(db.String(100))
    socioeconomic_vulnerability = db.Column(db.Float)
    heavy_rain_current = db.Column(db.Float)
    heavy_rain_future = db.Column(db.Float)
    dry_days_current = db.Column(db.Float)
    dry_days_future = db.Column(db.Float)
    hot_days_current = db.Column(db.Float)
    hot_days_future = db.Column(db.Float)
    humid_days_current = db.Column(db.Float)
    humid_days_future = db.Column(db.Float)
    tropical_nights_current = db.Column(db.Float)
    tropical_nights_future = db.Column(db.Float)
    climate_vulnerability = db.Column(db.Float)