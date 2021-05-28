from datetime import timedelta

from flask import Flask, session
from flask_migrate import Migrate,MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_script import Manager


app = Flask(__name__)


class config():
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


app.config.from_object(config)
db = SQLAlchemy(app)
sr = StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)
Session(app)
#创建管理器
mgr = Manager(app)
#初始化迁移器
Migrate(app,db)
# 创建迁移命令
mgr.add_command("mc",MigrateCommand)

@app.route('/')
def index():
    sr.set("name", "zs")
    session["name"] = "ls"
    return 'index11111'


if __name__ == '__main__':
    mgr.run()
