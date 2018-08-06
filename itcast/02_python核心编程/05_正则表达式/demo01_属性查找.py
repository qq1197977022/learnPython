class F(object):
    def __init__(self):
        self.a = 'F'


class A(F):
    def __init__(self):
        super(A, self).__init__()
        self.a = 'A'


class B(F):
    def __init__(self):
        super(B, self).__init__()
        self.a = 'B'


class C(A, B):
    a = 'C_类对象属性'

    def __init__(self):
        super(C, self).__init__()
        # self.a = 'C'

    def __getattr__(self, item):
        return 233333


c = C()
# print(c.a)
# print(C.__mro__)
# print(C.mro())
#
# print(F.__subclasses__())
# print(C.__bases__)
#
# print(f'{"类对象":-^60}')
# for i in C.__dir__(c):
#     print(i)
# else:
#     print('*'*30)
#
# for i in C.__dict__:
#     print(i)
# else:
#     print('*'*30)
#
# print(f'{"实例对象":-^60}')
# for i in c.__dir__():
#     print(i)
# else:
#     print('*'*30)
#
# for i in c.__dict__:
#     print(i)
# else:
#     print('*'*30)

print(f'{"访问不存在属性":-^60}')
print(c.a)
print(c.A)




































