# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import config

app = Flask(__name__)
app.config.from_object(config)
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

# 不要在生成db之前导入注册蓝图。
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
# 注册路由蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

# app 路由
from app import views
