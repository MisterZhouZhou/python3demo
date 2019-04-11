#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open('foo.txt', 'w')
fo.write('www.runoob.com!\nVery good site!\n')
# 关闭文件
fo.close()

print('-------文件已关闭----------')

print('-------开始读文件----------')
fo2 = open('foo.txt', 'r+')
content = fo2.read()
print(content)
fo2.close()