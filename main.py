# from datetime import timedelta
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
# from flask_sqlalchemy import SQLAlchemy
# from redis import StrictRedis
# from flask_session import Session
from flask_script import Manager
# from config import DevelopConfig
from info import create_app
from flask import Blueprint
# 利用模块创建app
app = create_app("dev")
# 创建管理器
mgr = Manager(app)

# 创建迁移命令
mgr.add_command("mc", MigrateCommand)



if __name__ == '__main__':
    mgr.run()
