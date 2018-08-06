class Foo(object):
    def __init__(self, name):
        self.name = name

    def _f1(self):
        print(self.name)

    def __f2(self):
        print(self.name)

    def f3(self):
        self.__f2()


foo = Foo("张三")

foo._f1()    # protect

# foo.__f2()    # private
# foo._Foo__f2() 利用其名称变形规则也可以实现对私有成员的访问

foo.f3()    # public
