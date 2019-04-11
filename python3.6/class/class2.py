#! /usr/bin/python3

class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, -4.5)
print(x.r,x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()