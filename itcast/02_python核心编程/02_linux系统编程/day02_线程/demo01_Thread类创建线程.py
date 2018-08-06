from threading import Thread
import time


def fun1():
    print('-'*30)
    time.sleep(1)


print('*' * 15)

if __name__ == '__main__':
    for i in range(5):

        # fun1()    # 单线程

        t = Thread(target=fun1)    # 多线程
        t.start()

print('=' * 15)


# 进程: 资源分配基本单位 ~ 容器
# 线程: CPU调度基本单位





