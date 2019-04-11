#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
# print(re.match('www', 'www.runoob.com'))
# print(re.match('www', 'www.runoob.com').span())





# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
# else:
#    print "No match!!"





# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配








# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "",phone)
# print('电话号码是：%s' %num)
#
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print "电话号码是 : ", num







# s = 'A23G4HFD567'
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value*2)
# print(re.sub('(?P<value>\d)', double ,s))






# pattern = re.compile(r'\d+')
# m = pattern.match('one12twothree34four')
# print(m)
#
#
# m2 = pattern.search('one12twothree34four').span()
# print(m2)
#
#
# m2 = re.search(r'\d+','one12twothree34four').span()
# print(m2)





# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print(m.groups())





# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)







# it = re.finditer(r"\d+","12a32bc43jf3")
# for match in it:
#     print (match.group() )





# it = re.split('\W+', 'runoob, runoob, runoob.')
# print(it)






