from pywifi import *

class PoJie():
    def __init__(self, path):
        self.path = path

    def show(self):
        print(self.path)


# if __name__ == '__main__':

start = PoJie('dd')
start.show()
