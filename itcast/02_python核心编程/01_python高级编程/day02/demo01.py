# gen_iter = (x for x in range(9, 20))
# print(type(gen_iter), gen_iter)
#
# for i in gen_iter:
#     print(i)
#
#
# def fib1():
#     a, b = 0, 1
#     for i in range(10):
#         print(b)
#         a, b = b, a+b
#
#
# fib1()
# print(type(fib1))


def fib2():
    a, b = 0, 1
    for i in range(10):
        c = yield b
        a, b = b, a+b
        if c is None:
            print('---------')


# for i in fib2():
#     print(i)
# print(type(fib2()), fib2())
a = fib2()
next(a)
# next(a)
# next(a)
# next(a)


print(type(a), type(fib2), type(fib2()))







