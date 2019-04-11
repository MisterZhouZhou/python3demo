#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# a+可追加可写
# w+ 可写可读

document = open('fo.txt', 'a+')
print('文件名：%s' %document.name)

document.write('这是我创建的一个测试文件!\nwelcom!')
print(document.tell())
# 设置指针回到文件最初
document.seek(os.SEEK_SET)
# 读文件
content = document.read()
print(content)
# 关闭文件
document.close()