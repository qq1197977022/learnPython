# 通用装饰器
# 通用装饰器
# 通用装饰器
# 通用装饰器
# 通用装饰器


def dec1(fun):    # 1.适用于有参函数的装饰器
    print("适用于有参函数的装饰器")

    def inner(arg):
        fun(arg)
    return inner


def dec2(fun):    # 2.适用于无参函数的装饰器
    print("适用于无参函数的装饰器")

    def inner():
        fun()
    return inner


def dec3(fun):    # 3.适用于有返回值函数的装饰器
    print("适用于有返回值函数的装饰器")

    def inner():
        r = fun()
        return r
    return inner


def dec4(fun):
    print("通用装饰器")

    def inner(*args, **kwargs):
        r = fun(*args, **kwargs)
        return r
    return inner


@dec1    # 特定装饰器
# @dec4    # 通用装饰器
def f1(arg1):
    print(arg1)


@dec2    # 特定装饰器
# @dec4    # 通用装饰器
def f2():
    print("无参函数")


@dec3    # 特定装饰器
# @dec4    # 通用装饰器
def f3():
    return "返回值"


f1("有参函数")

f2()

ret = f3()
print(ret)


