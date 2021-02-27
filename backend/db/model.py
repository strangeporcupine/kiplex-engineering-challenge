from backend.api import db

class RaceEvent(db.model):
    __tablename__ = 'race_events'
    
    id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.String(140))
    c_id = db.Column(db.String(140))
    start_time = db.Column(db.DateTime, index=True)
    start_point = db.Column(db.String(140))
    start_point_type = db.Column(db.String(140))
    end_time = db.Column(db.DateTime, index=True)
    end_point = db.Column(db.String(140))
    end_point_type = db.Column(db.String(140))
    status = db.Column(db.String(140))
