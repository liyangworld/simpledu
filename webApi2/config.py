import os

class BaseConfig(object):
    """ 配置基类 """
    SECRET_KEY = os.urandom(24)

    # 处理中文的(返回中文而非unicode)
    RESTFUL_JSON = dict(ensure_ascii=False)

    COUNTS_PER_PAGE = 10

class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/simpledu?charset=utf8'


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

