from backend.api import db, create_app
from backend.db.model import *

def initialize_tables():
    db.create_all(app=create_app())

def get_db_engine():
    db.__init__(app=create_app())
    return db