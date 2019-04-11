#!/usr/bin/python3

class Person:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说：我今年 %d 岁。' %(self.name, self.age))


class Student(Person):
    grade = ''
    def __init__(self, n, a, w, g):
        Person.__init__(self, n,a,w)
        self.grade = g

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class Speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class Sample(Speaker, Student):
    a = ''
    def __init__(self, n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)



p = Person('runoob', 10, 30)
p.speak()


s = Student('ken',10,60,3)
s.speak()


sam = Sample('zw', 22, 120, 6, 'tw')
sam.speak()
