#!/usr/bin/python
#coding=utf-8

# count = 0
# while(count<9):
#     print('The count is :', count)
#     count += 1
# print('Good bye!')




# exit = 1
# while exit != 0:
#     exit = raw_input("Enter a number: ")
#     print('You entered: ', exit)
# else:
#     print("Good bye")




# for letter in 'Python':  # 第一个实例
#     print '当前字母 :', letter
#
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#     print '当前水果 :', fruit
#
# print "Good bye!"





# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print '当前水果 :', fruits[index]
#
# print "Good bye!"


# print(range(10,20))




# # 查找10-20间的因式分解
# for num in range(10,20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print("%d 等于 %d * %d" % (num, i, j))
#             break
#     else:
#         print num, '是一个质数'




# # 查找素数
# i = 2
# while(i<100):
#     j = 2
#     while(j<= (i/j)):
#         if not(i%j): break
#         j += 1
#     if (j > i/j):
#         print('%d是素数' % (i))
#     i+= 1



# for letter in 'python':
#     if letter == 'h':
#         break
#     print('当前字母： %s' % letter)
#
#
# var = 10
# while var >0:
#     print('当前变量值: %s' % var)
#     var -= 1
#     if var == 5:
#         break
# print("Good bye!")




# print "My name is %s and weight is %d kg!" % ('Zara', 21)


list1 = ['physics', 'chemistry', 1997, 2000]

print list1
del list1[2]
print "After deleting value at index 2 : "
print list1