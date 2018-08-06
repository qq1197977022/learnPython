def dec(fun):
    print('***'*20)

    def inner():
        # 验证1
        print('+++验证+++')
        fun()

    return inner


def f1():
    print('------1------')


@dec    # 装饰器语法糖
def f2():
    print('------2------')


def f3():
    print('------3------')


def f4():
    print('------4------')


# 原业务
f1()

# 新需求,添加验证,开放封闭原则(对扩展开放,对修改封闭) ~ 装饰器
# 装饰器原理
f1 = dec(f1)
f1()


# 装饰器语法糖
f2()


# 彻底理解 ~ LowB故事


