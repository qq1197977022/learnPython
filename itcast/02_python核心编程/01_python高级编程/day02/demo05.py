# 闭包应用
def outer(k, b):
    def inner(x):
        print(k*x+b)
        print(id(k), id(b))
    return inner


# 外层函数确定曲线,内层函数求函数值
line1 = outer(1, 2)
line2 = outer(2, 4)

# 闭包简化调用过程
line1(3)
line2(3)

line1(4)
line2(4)
print('*'*30)


# 常规方式
def line(k, b, x):
    print(k*x + b)


# 对于已经确定的曲线,求函数值是k, b参数不是必须的,但这种调用方式必须每次重复传入
line(1, 2, 3)
line(2, 4, 3)

line(1, 2, 4)
line(2, 4, 4)


# 从地址的角度在分析一遍 ~ 第一次inner和第二次inner中k, b指向对象不同
# 哈哈... 已解决 ~ id()函数
