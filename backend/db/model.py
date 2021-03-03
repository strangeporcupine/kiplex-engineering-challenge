from backend.api import db

class RaceEvent(db.Model):
    __tablename__ = 'race_events'
    
    id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = db.relationship('Car', back_populates='race_times')
    start_time = db.Column(db.DateTime(timezone=True), index=True)
    start_point_id = db.Column(db.Integer, db.ForeignKey('track_sections.id'))
    start_point = db.relationship('TrackPoint')
    end_time = db.Column(db.DateTime(timezone=True), index=True)
    end_point_id = db.Column(db.Integer, db.ForeignKey('track_sections.id'))
    end_point = db.relationship('TrackPoint')
    status_id = start_point_id = db.Column(db.Integer, db.ForeignKey('race_status.id'))
    status = db.relationship('RaceStatus')

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(140))
    version = db.Column(db.String(140))
    race_times = db.relationship('RaceEvent', back_populates='car')

class TrackPoint(db.Model):
    __tablename__ = 'track_sections'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(140))
    track_type = db.Column(db.String(140))

class RaceStatus(db.Model):
    __tablename__ = 'race_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))