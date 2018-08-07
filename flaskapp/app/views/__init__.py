from app.views.async_handler import cly as _cly
from app.views.error_handler import error as _error
from app.views.index_hander import index as _index
from app.views.rest_clazz_handler import clazz as _clazz
from app.views.rest_login_handler import login as _login
from app.views.rest_school_handler import school as _school
from app.views.rest_user_handler import user as _user
from ..common import ConsoleLogger, relative_path

logger = ConsoleLogger(relative_path(__file__))
logger.info('initial app views model')

BLUEPRINT_MODELS = [
    _error,
    _index,
    _login,
    _user,
    _clazz,
    _school,
    _cly,
]