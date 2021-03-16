from backend.db.model import RaceEvent


def calculate_average_loop_time(v_id):
    # Query for race_times
    race_time_query = RaceEvent.query.filter_by(v_id=v_id)
    
    pass