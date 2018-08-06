def fun1(arg1, arg2):
    def dec(fun):
        def inner():
            print("权限验证...日志记录")
            if (arg1 + arg2) % 2 == 0:
                fun()
            else:
                fun()
                fun()
        return inner
    return dec


# 带参数装饰器
#   1.先调用,返回结果作为装饰器
#   2.可满足,同一装饰器对不同函数进行不同装饰 ~ 根据输入参数信息不同,返回不同装饰结果


@fun1(1, 3)
def f1():
    print("---f1---")


@fun1(1, 2)
def f2():
    print("===f2===")


f1()
f2()
print('-' * 30)

# -----------------------------------------------------------------------------同上 ~ 只是把条件判断和装饰器分离


def dec1(fun):
    def inner():
        print("权限验证...")
        fun()
    return inner


def dec2(fun):
    def inner():
        print("日志记录...")
        fun()
    return inner


def f(arg):
    if arg % 2 == 0:
        return dec1
    else:
        return dec2


@f(3)
def f3():
    print("~~~f3~~~")


@f(4)
def f4():
    print("***f4***")


f3()
f4()






