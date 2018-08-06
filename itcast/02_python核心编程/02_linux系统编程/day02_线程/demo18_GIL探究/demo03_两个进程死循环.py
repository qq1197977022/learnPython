import multiprocessing


def fun():
    while True:
        pass
    # print(multiprocessing.current_process().name)


def main():
    p = multiprocessing.Process(target=fun)
    p.start()

    while True:
        pass
    # print(multiprocessing.current_process().name)


if __name__ == '__main__':
    main()


# 单核CPU下, CPU占用100%
# 双核CPU下, 两CPU均占用100%

# 对比demo01, ...02, ...03总结
# 	1.多进程实现多任务比多线程效率高
# 