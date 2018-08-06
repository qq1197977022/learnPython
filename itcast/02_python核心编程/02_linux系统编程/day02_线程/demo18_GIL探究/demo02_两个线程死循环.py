import threading


def fun():
    while True:
        pass
    # print(threading.current_thread().name)


def main():
    t = threading.Thread(target=fun)
    t.start()

    while True:
        pass
    # print(threading.current_thread().name)


if __name__ == '__main__':
    main()


# 单核CPU下, CPU占用100%
# 双核CPU, 两个CPU各占50%

# ------------------------------------------------------
# CPython解释器使用GIL机制保证同一时刻只有一个线程执行Python bytecode
# 	1.python源代码被编译为bytecode
# 	2.bytecode是python程序在CPython解释器中的内部表现
# 	3.bytecode也会缓存在.pyc文件, 以便第二次执行同一文件时更快(避免重复编译), 这种“中间语言”被称之为运行在执行对应于每个字节码的机器码的虚拟机上
# 	4.需要注意的是: bytecode不能在不同的Python虚拟机运行, 在不同pytho版本之间也不稳定
# 这通过使对象模型(包括内置类型)隐式地避免并发访问来简化CPython实现
# 
# 锁定整个解释器使得解释器更易于多线程化, 而牺牲了多处理器机器提供的的大部分并行性
# ------------------------------------------------------
# ------------------------------------------------------
# 然而， 一些进行密集型计算任务的标准库或第三方模块, 被设计来释放GIL
# 	1.eg.压缩, 哈希
# 处理I/O时， GIL总是被释放
# ------------------------------------------------------
# 
# 
# 






