class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name}吃饭...')


def f0():
    print(f'{"函数":*^30}')


@staticmethod
def f1():
    print(f'{"静态方法":*^30}')    # 吐槽: 为什么静态方法对象是函数????? ---> <function f1 at 0x0000017290DF2EA0>


@classmethod
def f2(cls):
    print(f'{cls.__name__:*^30}')


# 给类对象添加函数
print('-' * 60, '给类对象添加函数')
Person.f0 = f0
Person.f0()
print(Person.f0)


# 给类对象添加静态方法
print('-' * 60, '给类对象添加静态方法')
Person.f1 = f1
Person.f1()
print(Person.f1)


# 给类对象添加类方法
print('-' * 60, '给类对象添加类方法')
Person.f2 = f2
Person.f2()
print(Person.f2)


# https://www.jianshu.com/p/212b6fdb2c50 静态方法和类方法
