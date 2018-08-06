import os
g_num = 100
ret = os.fork()
if ret == 0:
    print(f'{"A--->process1":-<30}{g_num:-<10}{id(g_num)}')
else:
    print(f'{"A--->process2":=<30}{g_num:-<10}{id(g_num)}')


print('*' * 30)


if ret == 0:
    g_num += 1
    print(f'{"B--->process1":-<30}{g_num:-<10}{id(g_num)}')
else:
    g_num += 2
    print(f'{"B--->process2":=<30}{g_num:-<10}{id(g_num)}')


# 各进程不共享全局变量, 因为个进程独立运行互相隔离, 每个进程都是一个单独的容器
# 解决办法
#   1.单台PC: 进程通信
#   2.多态PC: 网络通信 + 进程通信
