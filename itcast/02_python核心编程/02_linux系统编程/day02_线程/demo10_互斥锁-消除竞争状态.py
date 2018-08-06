from threading import Thread, Lock

g_num = 0


def fun1():
    global g_num
    mutex.acquire()    # 获取锁, 并阻塞
    for i in range(1000000):
        g_num += 1
    print(f'线程1{g_num:+>20}\t{id(g_num)}')
    mutex.release()    # 释放锁

    # with mutex:   # 带有acquire和release方法的对象可作为with语句的上下文管理器, 进入/离开语句块时acquire/release方法会自动调用
    #     for i in range(1000000):
    #         g_num += 1
    #     print(f'线程1{g_num:+>20}\t{id(g_num)}')


def fun2():
    global g_num
    mutex.acquire()    # 获取锁, 并阻塞
    for i in range(1000000):
        g_num += 1
    print(f'线程2{g_num:*>20}\t{id(g_num)}')
    mutex.release()  # 释放锁

    # with mutex:   # 带有acquire和release方法的对象可作为with语句的上下文管理器, 进入/离开语句块时acquire/release方法会自动调用
    #     for i in range(1000000):
    #         g_num += 1
    #     print(f'线程2{g_num:*>20}\t{id(g_num)}')


if __name__ == '__main__':
    mutex = Lock()

    print(f'主线程{g_num:->50}\t{id(g_num)}')

    p1 = Thread(target=fun1)
    p1.start()

    print(f'主线程{g_num:->60}\t\t{id(g_num)}')

    p2 = Thread(target=fun2)
    p2.start()

    print(f'主线程{g_num:->70}\t{id(g_num)}')


