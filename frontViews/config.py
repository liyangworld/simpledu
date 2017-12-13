
import os

class BaseConfig(object):
    """ 配置基类 """
    SECRET_KEY = os.urandom(24)
    RESTFUL_JSON = dict(ensure_ascii=False)

class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = False


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

