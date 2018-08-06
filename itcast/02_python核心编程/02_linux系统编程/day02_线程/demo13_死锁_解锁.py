import threading
import time


class SubThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(f'{"线程一":->60}')
            time.sleep(1)
            if mutexB.acquire():
                mutexA.release()
            mutexB.release()


class SubThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(f'{"线程二":=>60}')
            time.sleep(1)
            if mutexA.acquire():
                mutexB.release()
            mutexA.release()


if __name__ == '__main__':
    mutexA = threading.Lock()
    mutexB = threading.Lock()

    t1 = SubThread1()
    t2 = SubThread2()

    t1.start()
    t2.start()


# 避免死锁
#   1.银行家算法
#   2.设置超时
































