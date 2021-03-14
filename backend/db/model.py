from backend.api import db
from flask import url_for


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        print(kwargs)
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

class RaceEvent(db.Model, PaginatedAPIMixin):
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

    def duration_in_secs(self):
        time_taken =  self.end_time-self.start_time
        total_seconds = time_taken.total_seconds()
        return total_seconds

    def to_dict(self):
        return {
            'id': self.id,
            'car_model': self.car.model,
            'car_version': self.car.version,
            'start_point': self.start_point.label,
            'start_point_type': self.start_point.track_type,
            'end_point': self.end_point.label,
            'end_point_type': self.end_point.track_type,
            'status': self.status.name,
            'duration': self.duration_in_secs()
        }

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(140))
    version = db.Column(db.String(140))
    race_times = db.relationship('RaceEvent', back_populates='car')

    def to_dict(self):
        return {
            'id': self.id,
            'car_model': self.model,
            'car_version': self.version,
        }

class TrackPoint(db.Model):
    __tablename__ = 'track_sections'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(140))
    track_type = db.Column(db.String(140))

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'track_type': self.track_type,
        }

class RaceStatus(db.Model):
    __tablename__ = 'race_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.status,
        }


class AverageLoopTimes(db.Model):
    __tablename__ = 'average_loop_times'

    id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    average_time = db.Column(db.Integer)
