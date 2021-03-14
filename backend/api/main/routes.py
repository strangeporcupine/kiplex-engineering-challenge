from backend.db.model import Car, RaceEvent, RaceStatus, TrackPoint
from backend.api.main import bp
from flask import json, jsonify, request, current_app

@bp.route('/get_section_time', methods=['GET'])
def get_section_time():
    page=request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), current_app.config['PAGINATION_MAX_PAGE'])

    # Query for race_times
    race_time_query = RaceEvent.query

    data = RaceEvent.to_collection_dict(race_time_query, page, per_page, 'main.get_section_time')
    return jsonify(data)

@bp.route('/get_section_time/<int:v_id>', methods=['GET'])
def get_section_time_by_car(v_id):
    page=request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), current_app.config['PAGINATION_MAX_PAGE'])
    start_point_type=request.args.get('start_point_type', '', type=str)
    print(start_point_type)
    end_point_type=request.args.get('end_point_type', '', type=str)
    print(end_point_type)
    status = request.args.get('status', '', type=str)
    print(f'STATUS:{status}')

    # Query for race_times
    race_time_query = RaceEvent.query.filter_by(v_id=v_id)
    if status:
        race_time_query = race_time_query.filter(RaceEvent.status.has(name=status))
    if start_point_type:
        race_time_query = race_time_query.filter(RaceEvent.start_point.has(track_type=start_point_type))
    if end_point_type:
        race_time_query = race_time_query.filter(RaceEvent.end_point.has(track_type=end_point_type))

    data = RaceEvent.to_collection_dict(
        race_time_query,
        page,
        per_page,
        f'main.get_section_time_by_car',
        v_id=v_id,
        start_point_type = start_point_type,
        end_point_type=end_point_type,
        status=status
        )
    return jsonify(data)

@bp.route('/get_average_loop_time', methods=['GET'])
def get_average_loop_time(v_id):
    pass

@bp.route('get_cars', methods=['GET'])
def get_cars():
    cars = Car.query.with_entities(Car.version).distinct(Car.version)
    return jsonify([c[0] for c in cars])

@bp.route('get_track_section_types', methods=['GET'])
def get_track_section_types():
    track_points = TrackPoint.query.with_entities(TrackPoint.track_type).distinct(TrackPoint.track_type)
    return jsonify([t[0] for t in track_points])

@bp.route('get_status', methods=['GET'])
def get_status():
    status_types = RaceStatus.query.with_entities(RaceStatus.name).distinct(RaceStatus.name)
    return jsonify([s[0] for s in status_types])
