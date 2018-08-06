import multiprocessing
import time


def read(queue):
    while True:
        if not queue.empty():
            item = queue.get()
            print(f'get {item} from the queue')
            # time.sleep(2)
        else:
            print(f'{"消费者":*>60}')
            time.sleep(3)


def write(queue):
    while True:
        for item in 'ABC':
            if not queue.full():
                queue.put(item)
                print(f'put {item} into the queue')
                # time.sleep(1)
            else:
                print(f'{"生产者":->60}')
                time.sleep(2)


q1 = multiprocessing.Queue(3)
pr = multiprocessing.Process(target=read, args=(q1,))   # 消费者
pw = multiprocessing.Process(target=write, args=(q1,))  # 生产者


if __name__ == '__main__':
    pw.start()
    pr.start()
    print('主进程执行完毕')


'''
1.各进程独立运行, 互相隔离
2.进程间通信
    1.通常使用进程间消息传递实现进程间通信而避免使用类似锁这样的同步原语
    2.传递消息方式
        1.Pipe管道: 连接两个进程
            1.命名管道
            2.无名管道
        2.Queue队列: 允许多生产者和消费者
        3.共享内存/内存映射
        4.网络socket通信
'''



















































































