import multiprocessing
import time


def fun1():
    time.sleep(5)
    print(f'{"子进程A":-<30}结束')


def fun2():
    time.sleep(10)
    print(f'{"子进程B":-<30}结束')


p1 = multiprocessing.Process(target=fun1)
p2 = multiprocessing.Process(target=fun2)


if __name__ == '__main__':
    p1.start()
    p2.start()
    print('父进程执行完毕，等待子进程结束')


# 父进程等待子进程结束 ~ 这点与类Unix平台下直接使用fork函数不同
# 为什么要等待?
#   1.回收子进程资源
#       1.僵尸进程: 子进程结束, 父进程回收子进程资源之前, 此期间内子进程状态
#       2.孤儿进程: 父进程先结束, 子进程没结束, 此时子进程变为孤儿进程
#           1.由PID=1的进程回收其资源
#   2.特殊进程
#       1.PID=0操作系统启动即创建, 管理进程资源
#       2.PID=1间接/直接创建子进程
#























































































