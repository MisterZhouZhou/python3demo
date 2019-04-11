#! /usr/bin/python3
# 文件名: class1.py

class MyClass:
    ''' 一个简单的类实例 '''
    i = 12345
    def f(self):
        return 'hello world!'

# 实例化类
x = MyClass()
print("类的属性i为：", x.i)
print('类的方法f输出为：', x.f)