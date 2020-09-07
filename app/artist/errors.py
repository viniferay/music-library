from http.client import HTTPException

from flask import jsonify

from app.artist import bp


@bp.app_errorhandler(HTTPException)
def handle_error(e):
    return jsonify(error=e.description), e.code


@bp.app_errorhandler(Exception)
def handle_error(e):
    code = 500
    return jsonify(error=str(e)), code
