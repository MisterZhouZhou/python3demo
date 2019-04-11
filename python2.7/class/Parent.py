#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    '定义父类'
    parentAttr = 100
    def __init__(self):
        print('调用父类构造函数')

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):
    def __init__(self):
        print('调用子类构造函数')

    def childMethod(self):
        print('调用子类方法')


