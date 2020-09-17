from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers  # pylint: disable=unused-import,wrong-import-position
