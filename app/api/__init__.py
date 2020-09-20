from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens  # pylint: disable=unused-import,wrong-import-position
