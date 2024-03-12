from db import db


class TrackingGoalsModel(db.Model):
    __tablename__ = "tracking goals"

    id = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.String, nullable=False)
    current_weight = db.Column(db.Float, nullable=False)
    weight_goal=db.Column(db.Float, nullable=False)



