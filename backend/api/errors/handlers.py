from backend.api.errors.error import error_response
from backend.api import db
from backend.api.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return error_response(404)


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response(500)