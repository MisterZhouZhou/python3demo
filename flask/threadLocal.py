# 线程全局变量
import threading

localobj = threading.local()

def threadfunc(name):
    localobj.name = name
    print('localojb.name is %s' %name)

if __name__ == '__main__':
    t1 = threading.Thread(target=threadfunc, args=('Hyman',))
    t2 = threading.Thread(target=threadfunc, args=('zw',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

