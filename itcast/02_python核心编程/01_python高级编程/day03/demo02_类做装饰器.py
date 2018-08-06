class Dec(object):
    def __init__(self, fun):
        print('初始化')
        self.__fun = fun

    def __call__(self, *args, **kwargs):    # 使实例对象callable
        self.__fun()


@Dec    # 类做装饰器
def f1():
    print('被装饰函数执行...')
# f1 = Dec(f1)


f1()

