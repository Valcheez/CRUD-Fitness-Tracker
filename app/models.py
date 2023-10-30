from app import db

class FitnessEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date, nullable=False)
    workout = db.Column(db.String(100), nullable=False)
    exercises = db.Column(db.String(500), nullable=True)
