import os

environ = os.environ
PROJECT_PATH = os.path.join(os.path.dirname(__file__),"app")
TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, "templates")
STATIC_FOLDER = os.path.join(PROJECT_PATH, "static")
DEBUG = True  # open debug /or hot restart

# ****** 上传配置
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sql'}

# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/t dest.db'

# ****** MySQL 配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    user=environ.get('DB_USER', 'root'),
    password=environ.get('DB_PASS', 'zw123456'),
    host=environ.get('DB_HOST', 'localhost'),
    port=environ.get('DB_PORT', 3306),
    database=environ.get('DB_NAME', 'test'))
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 禁止警告
SQLALCHEMY_ECHO = False  # 是否打印
#SQLALCHEMY_POOL_SIZE = 15  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
#SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10。
#SQLALCHEMY_POOL_RECYCLE = 60 * 60 * 2  # 自动回收连接的秒数。
#SQLALCHEMY_MAX_OVERFLOW = 0  # 控制在连接池达到最大值后可以创建的连接数。

# ****** Celery 配置 celery.app.utils.py
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_BROKER_URL = 'redis://localhost:6379'

# ############################## flask project auto config ######################################
DOWNLOAD_FOLDER = '/tmp'
HOME_PATH = '/'

# ############################## flask start config ######################################
HOST = '0.0.0.0'
PORT = 5000