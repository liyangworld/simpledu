
from .admin import admin

from .home import home
from .course import course
from .live import live


from .user import user

from flask import render_template

def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(course)
    app.register_blueprint(live)
    app.register_blueprint(admin)
    app.register_blueprint(user)

def register_errors(app):

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def permisson_denied(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


