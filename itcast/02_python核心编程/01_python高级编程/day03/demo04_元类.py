# __new__()主要目的是用于不可变类型(eg.int, str, tuple)实例对象的自定义创建
# metaclass主要目的是自定义类对象自定义创建


class Foo(object):
    def __init_subclass__(cls, **kwargs):   # 被继承时自动调用
        print('小猪佩奇身上纹')
        cls.__name__ = '333'


class Sub(Foo):
    print('掌声送给社会人')
    pass



