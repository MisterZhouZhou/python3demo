import os
# 用于连接数据的数据库。
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ty158917@139.199.189.211:3306/movie"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:zw123456@127.0.0.1:3306/movie"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
SQLALCHEMY_TRACK_MODIFICATIONS = True
REDIS_URL = "redis://127.0.0.1:6379/0"
SECRET_KEY = 'mtianyan_movie'
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/")
P_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/pmovies/")   # 电影预告上传路径
M_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/movies/")    # 电影上传路径
FC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/users/")