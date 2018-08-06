class Foo(object):
    def __getattr__(self, item):
        print(item, end=' ')
        return self


foo = Foo()
print(foo.a.b.c)


print(Foo.__name__)
print(Foo.__qualname__)























