from threading import Thread
import time

g_num = 0


def fun1():
    global g_num
    for i in range(1000000):
        g_num += 1
        # print(f'{id(g_num):->60}')
    print(f'线程1{g_num:+>20}\t{id(g_num)}')


def fun2():
    global g_num
    for i in range(1000000):
        g_num += 1
        # print(f'{id(g_num):*>60}')
    print(f'线程2{g_num:*>20}\t{id(g_num)}')


if __name__ == '__main__':
    print(f'主线程{g_num:->50}\t{id(g_num)}')

    p1 = Thread(target=fun1)
    p1.start()

    print(f'主线程{g_num:->60}\t\t{id(g_num)}')

    time.sleep(5)   # 延时, 保证线程1执行完毕

    p2 = Thread(target=fun2)
    p2.start()

    print(f'主线程{g_num:->70}\t{id(g_num)}')


# 问题:
#   1.共享资源竞争
#   2.为什么设置延时后线程1, 2中g_num的地址相同 反之则不同?
#   3.rang范围 100, 1000, 1... id值也不同...
#   4.晕...

































































































