from multiprocessing import Process
import os
import time


class P(Process):
    def __init__(self):
        super(P, self).__init__()
        pass

    def run(self):
        while True:
            print('子进程', os.getpid(), os.getppid())
            time.sleep(1)


if __name__ == '__main__':
    p1 = P()
    p1.start()

    while True:
        print('父进程', os.getpid(), os.getppid())
        time.sleep(1)






