a = chr(97)
print(a)
b = ord(a)
print(b)

c = pow(2, 3, 3)
print(c)

print(round(123.456789, 3))

print(sum((1, 2, 3, 4, 5), 15))    # 累加求和 ~ 数字累加

print(sum([(1,), (2,), (3,)], (4,)))    # 累加求和 ~ 元组累加


class F(object):
    a = 3

    def f(self):
        pass


f1 = F()
print(F.__dict__)
print(vars(F))































