import shutil
import os
import multiprocessing
import time


def producer(que):
    dir_entry = os.scandir('D:\\software\\360\\360se6\\Application\\9.1.0.404')
    for entry in dir_entry:
        if entry.is_file():
            print(f'生产{entry.path:->60}')
            que.put(entry.path)


def consumer(que):
    count = 0
    while True:
        if que.empty():
            time.sleep(1)   # 不能直接退出, 可能只是暂时空
            count += 1
            if count == 3:  # 给三次机会, 出现三次为空, 说明任务完成
                break
        else:
            path = que.get()
            print(f'消费{path:=>60}')
            shutil.copy(path, 'C:\\Users\\kc\\Desktop\\0')


def main():
    que = multiprocessing.Queue(2)    # 阻塞队列

    p1 = multiprocessing.Process(target=producer, args=(que,))  # 创建进程实例对象
    p2 = multiprocessing.Process(target=consumer, args=(que,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()


# 待完善功能
#   1.递归拷贝子文件夹
#   2.任务是否真的完成, 通过三次机会看似可行, 但不够严谨; 是否完成因该由生产者线程说了算














