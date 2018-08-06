from threading import Thread

g_num = 0
g_flag = True


def fun1():
    global g_num
    global g_flag
    if g_flag:
        for i in range(1000000):
            g_num += 1
        g_flag = False
    print(f'线程1{g_num:+>20}\t{id(g_num)}')


def fun2():
    global g_num
    global g_flag
    # 轮询
    while True:    # 如果不要求实时, 设置休眠延时更好
        if not g_flag:
            for i in range(1000000):
                g_num += 1
            print(f'线程2{g_num:*>20}\t{id(g_num)}')
            break


if __name__ == '__main__':
    print(f'主线程{g_num:->50}\t{id(g_num)}')

    p1 = Thread(target=fun1)
    p1.start()

    print(f'主线程{g_num:->60}\t\t{id(g_num)}')

    p2 = Thread(target=fun2)
    p2.start()

    print(f'主线程{g_num:->70}\t{id(g_num)}')
