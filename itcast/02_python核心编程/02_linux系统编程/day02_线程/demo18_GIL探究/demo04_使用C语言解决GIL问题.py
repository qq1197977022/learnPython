import ctypes
import threading

# 创建共享库实例对象
# shared_lib_loader = ctypes.LibraryLoader()
# shared_lib = shared_lib_loader.LoadLibrary('./libDeadLoop.so')


def main():
    # 使用预置库加载器加载共享库
    shared_lib = ctypes.cdll.LoadLibrary('./libDeadLoop.so')

    t = threading.Thread(target=shared_lib.deadLoop)    # libDeadLoop共享库中函数
    t.start()

    while True:
        pass


if __name__ == '__main__':
    main()

# 双核CPU下， 两个CPU占用均100%
