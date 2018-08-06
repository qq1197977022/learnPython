import greenlet


def producer():
    f = open('D:\workspace\备忘.txt', 'rt', encoding='UTF8')
    while True:
        line = f.readline()
        if line == '':
            break
        print(f'producer: {line}')
        g2.switch(line)


def consumer(line):
    print(f'consumer: {line}')
    while True:
        line = g1.switch()
        print(f'consumer: {line}')


g1 = greenlet.greenlet(run=producer)
g2 = greenlet.greenlet(run=consumer)
g1.switch()    # 切换控制权
print('-'*50)   # 最后执行, 说明控制权切换到协程, 直到协程执行完毕


# 参考
#   1.PyPI: https://pypi.org/project/greenlet/
#     1.文档: https://greenlet.readthedocs.io/en/latest/

# greenlet是Stackless的一个分支, 是比micro-thread更原始的概念, 没有隐式调度 ~ 即coroutines(协程)
#
# Stackless
#   1.CPython的另一种实现, 支持被称为tasklets的micro-threads
#   2.tasklets以伪并发(通常是在单个或几个OS-level线程上运行)和通过channels进行异步数据交换的方式运行





