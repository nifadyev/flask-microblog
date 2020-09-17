from flask import render_template
from app import db
from app.errors import bp  # pylint: disable=unused-import


@app.errorhandler(404)
def not_found_error(_error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(_error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
