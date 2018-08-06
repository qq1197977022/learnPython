import multiprocessing
import time


def fun1():
    for i in range(10):
        print(f'p1{i:->10}')
        time.sleep(2)


def fun2():
    for i in range(10):
        print(f'p2{i:*>10}')
        time.sleep(2)


p1 = multiprocessing.Process(target=fun1)
p2 = multiprocessing.Process(target=fun2)

if __name__ == '__main__':
    for i in range(15):
        time.sleep(1)
        if i == 2:     # 同时启动进程p1, p2
            print(f'{"进程p1, p2 启动":-^30}')
            p1.start()
            p2.start()
        elif i == 8:   # 进程p2终止, 进程p1加锁
            print(f'{"进程p1加锁":-^30}')
            p1.join()   # 进程p1加锁, 直到结束, 父进程才会执行, 但不会影响兄弟进程的执行

        print(f'{"主进程":=^30}')
















































































