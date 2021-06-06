from datetime import timedelta

from redis import StrictRedis


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/info16"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    SECRET_KEY = "/A9rbIovhq6h7mFG4O59HXf1M+qFJxBvzCn4fPhZfpSHXuASEtzcj64Tm7LbQ5E3"
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class DevelopConfig(Config):
    DEBUG = True

class ProduceConfig(Config):
    DEBUG = False


congfig_dict = {"dev": DevelopConfig,
                "pro": ProduceConfig

           }
