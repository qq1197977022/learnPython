import threading
import time
import os

g_num = 100


def fun1():
    global g_num
    for i in range(3):
        g_num += 1
        print(id(g_num))
    print(f'线程1{g_num:->30}\t{id(g_num)}\t{os.getpid()}')


def fun2():
    global g_num
    print(f'线程2{g_num:=>30}\t{id(g_num)}\t{os.getpid()}')


if __name__ == '__main__':
    print(f'主线程{g_num:*>30}\t{os.getpid()}')

    t1 = threading.Thread(target=fun1)
    t1.start()

    time.sleep(1)

    t2 = threading.Thread(target=fun2)
    t2.start()


# 多线程共享全局变量
#   1.因为各子线程和主线程同属一个进程容器





