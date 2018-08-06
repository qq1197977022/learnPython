class Foo(object):
    def __call__(self):
        print('模仿callable对象')


foo = Foo()
foo()    # 使实例对象callable


# 参见Data model
