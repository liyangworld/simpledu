
from flask import Flask


from .config import configs
from .models import db
from .resources import add_resources



def create_app(config):
    """ 可以根据传入的 config 名称，加载不同的配置
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLAlchemy 的初始化方式改为使用 init_app
    db.init_app(app)
    add_resources(app)


    return app

