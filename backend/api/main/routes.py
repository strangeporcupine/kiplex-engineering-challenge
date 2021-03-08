from backend.db.model import Car, RaceEvent, RaceStatus, TrackPoint
from backend.api.main import bp
from flask import jsonify, request, current_app

@bp.route('/get_section_time', methods=['GET'])
def get_section_time():
    page=request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), current_app.config['PAGINATION_MAX_PAGE'])

    # Query for race_times
    race_time_query = RaceEvent.query

    data = RaceEvent.to_collection_dict(race_time_query, page, per_page, 'main.get_time_spent')
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