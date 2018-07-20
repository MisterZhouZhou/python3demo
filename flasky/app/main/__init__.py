from flask import Blueprint #蓝本

main = Blueprint('main',__name__)

from . import views, errors


