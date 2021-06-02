# from datetime import timedelta
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_script import Manager
from config import DevelopConfig

app = Flask(__name__)

app.config.from_object(DevelopConfig)
db = SQLAlchemy(app)
sr = StrictRedis(host=DevelopConfig.REDIS_HOST, port=DevelopConfig.REDIS_PORT)
Session(app)
# 创建管理器
mgr = Manager(app)
# 初始化迁移器
Migrate(app, db)
# 创建迁移命令
mgr.add_command("mc", MigrateCommand)


@app.route('/')
def index():
    sr.set("name", "zs")
    session["name"] = "ls"
    return 'index11111'


if __name__ == '__main__':
    mgr.run()
