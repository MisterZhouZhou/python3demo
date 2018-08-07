#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 16:25
# @Author  : TOM.LEE
# @File    : __init__.py.py
# @Software: PyCharm
import app.core.database
import app.core.http_handler
import app.core.http_interceptor
from ..common import ConsoleLogger, relative_path

logger = ConsoleLogger(relative_path(__file__))
logger.info('initial app core model')
