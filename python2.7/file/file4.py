#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open('test','w')
    fh.write('这是一个测试文件')
except IOError:
    print('Eror: 没有找到文件')
else:
    print('内容写入成功')
    fh.close()