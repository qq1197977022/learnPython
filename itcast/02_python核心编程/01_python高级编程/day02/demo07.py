def dec1(fun):
    print('------1------')

    def inner1():
        print('+++1+++')
        fun()
    return inner1


def dec2(fun):
    print('------2------')

    def inner2():
        print('+++2+++')
        fun()
    return inner2


@dec1
@dec2
def f1():
    print(3)

# f1 = dec1(dec2(f1))


f1()


# 执行过程
# @dec2
# 	1.dec2(fun = f1)
# 	2.print(------2------)
# 	3.f1 = inner2, fun = f1
# @dec1
# 	1.dec1(fun = inner2)
# 	2.print(------1------)
# 	3.f1 = inner1, fun = inner2
#
#
# f1() f1 = inner1
# 		1.print(+++1+++)
# 		2.fun() <~~~> inner2()
# 			1.print(+++2+++)
# 			2.fun() <~~~> f1()
# 				1.3
