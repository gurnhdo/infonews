#把视图函数封装成模块 需要使用蓝图
# 创建蓝图
from flask import Blueprint

home_blu = Blueprint("home_blue",__name__)

from .views import *