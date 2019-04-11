#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print('%s 销毁' % class_name)