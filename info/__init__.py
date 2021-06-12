from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from config import congfig_dict

sr = None #type:StrictRedis
db = None #type:SQLAlchemy

# 定义一个函数 让代码作为功能使用 不主动执行 封装起来让别的程序调用
# 工厂函数
def create_app(config_type):
    config_class=congfig_dict[config_type]


    app = Flask(__name__)
    global sr,db
    app.config.from_object(config_class)
    db = SQLAlchemy(app)
    sr = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    Session(app)
    # 初始化迁移器
    Migrate(app, db)

    from info.modules.home import home_blu
    app.register_blueprint(home_blu)

    return app
