from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes  # pylint: disable=unused-import,wrong-import-position
