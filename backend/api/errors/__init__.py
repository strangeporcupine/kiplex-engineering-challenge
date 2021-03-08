from flask import Blueprint

bp = Blueprint('errors', __name__)

from backend.api.errors import handlers