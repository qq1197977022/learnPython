class Foo(object):
    # 参见Data model ~ 自定义属性访问
    __slots__ = ('name', 'age')    # 显式声明数据成员,避免为每个instance对象创建__dict__和__weakref__,进而避免浪费空间

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f(self):
        print(self.name, self.age)


foo = Foo('张三', 28)
foo.f()

foo.name = '李四'
foo.age = 18
foo.f()


# foo.addr = '郑州'    AttributeError: 'Foo' object has no attribute 'addr'
# https://docs.python.org/3/reference/datamodel.html#slots




