#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午5:01
# @Author         : Tom.Lee
# @File           : __init__.py
# @Product        : PyCharm
# @Source         :

from app.models.clazz import Clazz
from app.models.school import School
from app.models.user import User
from ..common import ConsoleLogger, relative_path

logger = ConsoleLogger(relative_path(__file__))
logger.info('initial app models model')

__all__ = ['User', 'Clazz', 'School']

# models
MODELS = __all__
# blacklist = ['user']
