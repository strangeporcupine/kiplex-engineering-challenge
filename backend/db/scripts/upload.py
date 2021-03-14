#!/usr/bin/python

from backend.db.model import Car, RaceEvent, RaceStatus, TrackPoint
from backend.db.utils.connection import get_db_engine, initialize_tables
import csv
import logging
from datetime import datetime
import sys


DATETIME_FORMAT = r'%Y-%m-%d %H:%M:%S%z'

def load_race_csv(file):
    with open(file) as f:
        data = list(csv.reader(f, delimiter=','))
    logging.info(f'CSV file loaded. {len(data)} race data entries found.')
    return data

def valid_race_data(race_data):
    if '' in race_data or None in race_data:
        logging.error(f'Race data entry contains empty values: {race_data}')
        return False

    starttime = parse_race_datetime(race_data[2] +'00', DATETIME_FORMAT)  # 00 added to datestring to conform to timezone standard
    endtime = parse_race_datetime(race_data[5] +'00', DATETIME_FORMAT)  # 00 added to datestring to conform to timezone standard

    if not starttime or not endtime:
        return False
    return True

def add_race_data_to_db(db_engine, race_data):
    if valid_race_data(race_data):
        # Add car to database
        car_model = race_data[1]
        car_version = race_data[0]
        car = Car.query.filter_by(model=car_model, version=car_version).first()
        if car is None:
            car = Car(model=car_model, version=car_version)
            db_engine.session.add(car)
        
        # Add starting trackpoint
        start_track_label = race_data[3]
        start_track_type = race_data[4]
        starting_point = TrackPoint.query.filter_by(label=start_track_label, track_type=start_track_type).first()
        if starting_point is None:
            starting_point = TrackPoint(label=start_track_label, track_type=start_track_type)
            db_engine.session.add(starting_point)

        # Add end trackpoint
        end_track_label = race_data[6]
        end_track_type = race_data[7]
        end_point = TrackPoint.query.filter_by(label=end_track_label, track_type=end_track_type).first()
        if end_point is None:
            end_point = TrackPoint(label=end_track_label, track_type=end_track_type)
            db_engine.session.add(end_point)

        # Add Status
        status_type = race_data[8].strip().title()
        status = RaceStatus.query.filter_by(name=status_type).first()
        if status is None:
            status = RaceStatus(name=status_type)
            db_engine.session.add(status)

        # Add race event
        starttime = parse_race_datetime(race_data[2] +'00', DATETIME_FORMAT)  # 00 added to datestring to conform to timezone standard
        endtime = parse_race_datetime(race_data[5] +'00', DATETIME_FORMAT)  # 00 added to datestring to conform to timezone standard
        race_event = RaceEvent(
            start_time=starttime,
            start_point=starting_point,
            end_time=endtime,
            end_point=end_point,
            status=status
        )

        # Add data to database
        car.race_times.append(race_event)
        db_engine.session.commit()

    else:
        logging.info(f'Skipped entry: {race_data}')


def parse_race_datetime(timestamp, date_format):
    try:
        parsed_date = datetime.strptime(timestamp, date_format)
    except ValueError:
        logging.error(f'Failed to parse datetime for {timestamp}. Expected Format: {date_format}')
        parsed_date = None
    return parsed_date

if __name__ == '__main__':
    # Create tables if fresh installation
    initialize_tables()

    # Load csv file and add to database
    csv_file = sys.argv[1]
    data = load_race_csv(csv_file)
    db_engine = get_db_engine()
    for row in data:
        add_race_data_to_db(db_engine, row)
