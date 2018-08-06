# 闭包: 函数内部定义的函数和该函数所引用的外部变量统称为闭包


def fun1(num):
    print(num)
    return fun1    # 返回函数自身引用


fun1(11)(22)
print('*' * 30)


def outer1(num_out):
    print(num_out)

    def inner1(num_in):
        print(num_out + num_in)
    inner1(num_out)    # 调用内层函数


outer1(33)
print('*' * 30)


def outer2(num_out):
    print(num_out)

    def inner2(num_in):
        print(num_out + num_in)
    return inner2    # 返回内层函数引用


outer2(44)(55)
