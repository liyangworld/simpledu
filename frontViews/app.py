
from flask import Flask
from flask_login import LoginManager

from .config import configs
from .controllers import register_blueprints, register_errors
from .models import User

def register_extensions(app):

    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'home.login'
    login_manager.init_app(app)

    # 这个callback函数用于reload User object，根据session中存储的user_id
    @login_manager.user_loader
    def user_loader(user_id):

        return User.get(user_id)




def create_app(config):
    """ 可以根据传入的 config 名称，加载不同的配置
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_errors(app)
    register_blueprints(app)
    return app

