from flask import Blueprint

bp = Blueprint('artist', __name__)

from app.artist import controller
