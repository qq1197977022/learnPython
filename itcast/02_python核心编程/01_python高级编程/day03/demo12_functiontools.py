import functools


def f1(x, *args, **kwargs):
    y = kwargs['k']*x + kwargs['b']
    return y


p1 = functools.partial(f1, k=3, b=4)    # 第一条直线L1
y1 = p1(4)    # 求点x=4出的纵坐标
print(y1)

p2 = functools.partial(f1, k=5, b=2)    # 第二条直线L2
y2 = p2(4)    # 求点x=4出的纵坐标
print(y2)
print('-'*30)


def f2(arg1, arg2):
    ret = f'{arg1}---{arg2}'
    return ret


ret = functools.reduce(f2, 'abcd', 3)
print(ret)






















