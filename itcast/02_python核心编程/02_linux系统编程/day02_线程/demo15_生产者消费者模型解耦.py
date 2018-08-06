import queue
import threading
import time


def producer():
    while True:
        if que.qsize() < 2:    # 懒惰的生产者
            for i in range(2):
                que.put(f'{"生产数据":->40}\t{i}')
                print(f'{"生产数据":->40}\t{i}')
                time.sleep(0.1)


def consumer():
    while True:    # 积极的消费者
        print(f'消费{que.get()}')
        time.sleep(0.1)


if __name__ == '__main__':
    que = queue.Queue(10)

    pro = threading.Thread(target=producer)
    con = threading.Thread(target=consumer)

    for i in range(9):
        que.put(f'{"初始数据":->30}\t{i}')

    pro.start()
    con.start()


# 解决多线/进程协作, 但速度不匹配问题
#   1.生产者和消费者不直接通信, 而是通过像阻塞队列这样的缓冲区间接通信, 平衡生产者和消费者速度差


































































































