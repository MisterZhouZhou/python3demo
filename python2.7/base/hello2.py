#!/usr/bin/python
#coding=utf-8

# counter = 1000 #赋值
# miles = 1000.0 #浮点型
# name = "John"  #字符型
#
# print(counter)
# print(miles)
# print(name)
#
# a = b = c = 1
# print(a,b,c)
#
# a1,b1,c1 = 2,2,2
# print(a1,b1,c1)


# 字符串
# str = 'Hello World!'
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*2)
# print(str+"TEST")



#数组
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# print(list)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(tinylist*2)
# print(list+tinylist)


# a = 21
# b = 10
# c = 0
#
# if(a == b):
#     print('a 等于 b')
# else:
#     print "a 不等于 b"
#
# if (a != b):
#     print "a 不等于 b"
# else:
#     print "a 等于 b"
#
# if (a <> b):
#     print "3 - a 不等于 b"
# else:
#     print "3 - a 等于 b"
#
# if (a < b):
#     print "4 - a 小于 b"
# else:
#     print "4 - a 大于等于 b"
#
# if (a > b):
#     print "5 - a 大于 b"
# else:
#     print "5 - a 小于等于 b"
#
# # 修改变量 a 和 b 的值
# a = 5
# b = 20
# if (a <= b):
#     print "6 - a 小于等于 b"
# else:
#     print "6 - a 大于  b"
#
# if (b >= a):
#     print "7 - b 大于等于 a"
# else:
#     print "7 - b 小于 a"



# a = 10
# b = 20
#
# if (a and b):
#     print "1 - 变量 a 和 b 都为 true"
# else:
#     print "1 - 变量 a 和 b 有一个不为 true"
#
# if (a or b):
#     print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#     print "2 - 变量 a 和 b 都不为 true"
#
# # 修改变量 a 的值
# a = 0
# b = 20
# if (a and b):
#     print "3 - 变量 a 和 b 都为 true"
# else:
#     print "3 - 变量 a 和 b 有一个不为 true"
#
# if (a or b):
#     print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#     print "4 - 变量 a 和 b 都不为 true"
#
# if not (a and b):
#     print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
# else:
#     print "5 - 变量 a 和 b 都为 true"


# a = 10
# b = 20
# list = [1, 2, 3, 4, 5];
#
# if (a in list):
#     print "1 - 变量 a 在给定的列表中 list 中"
# else:
#     print "1 - 变量 a 不在给定的列表中 list 中"
#
# if (b not in list):
#     print "2 - 变量 b 不在给定的列表中 list 中"
# else:
#     print "2 - 变量 b 在给定的列表中 list 中"
#
# # 修改变量 a 的值
# a = 2
# if (a in list):
#     print "3 - 变量 a 在给定的列表中 list 中"
# else:
#     print "3 - 变量 a 不在给定的列表中 list 中"








# flag = False
# name = 'luren'
# if name == 'python':         # 判断变量否为'python'
#     flag = True          # 条件成立时设置标志为真
#     print 'welcome boss'    # 并输出欢迎信息
# else:
#     print name              # 条件不成立时输出变量名称





# num = 5
# if num == 3:            # 判断num的值
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:           # 值小于零时输出
#     print 'error'
# else:
#     print 'roadman'     # 条件均不成立时输出








# 例3：if语句多个条件
num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine


num = 4
if num > 0 & num < 5:
    print('d')
else:
    print('error')

if num > 0 and num < 5:
    print('d2')
else:
    print('error2')