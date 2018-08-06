import os, time
ret = os.fork()    # fork a child process, 仅适用于类Unix平台

print('fork函数返回值 = {}'.format(ret))

if ret == 0:
    print('当前进程(即子进程)pid---{0}父进程pid---{1}'.format(os.getpid(), os.getppid()))
else:
    print('当前进程(即父进程)pid============{0}父进程pid==={1}'.format(os.getpid(), os.getppid()))


'''https://baike.baidu.com/item/fork/7143171?fr=aladdin
1.分叉函数
    1.返回值
        1.成功调用
            1.向子进程返回0
            2.向父进程返回子进程PID
        2.失败返回-1
    2.作用: 将运行着的程序分成两个几乎完全一样的进程
        1.每个进程都启动一个从代码同一位置同时开始执行的线程,就像是同时启动了该应用程序的两个副本
'''









