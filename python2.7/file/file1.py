#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open('foo.txt', 'w')
print('文件名: %s' %fo.name)
print('是否已关闭: %s' %fo.closed)
print('访问模式: %s' %fo.mode)
print('末尾是否强制加空格: %s' %fo.softspace)
fo.close()
print('是否已关闭: %s' %fo.closed)