def f1(arg):
    if arg % 2 == 0:
        return True
    else:
        return False


tup1 = (1, 2, 3, 4, 5, False, 0)


print('---demo01---')
ft1 = filter(f1, tup1)
print(ft1)
print(*ft1)

print('---demo02---')
ft2 = filter(lambda x: x % 2 == 0, tup1)
print(ft2)
print(*ft2)


print('---demo03---')
ft3 = filter(None, tup1)    # If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
print(ft3)                     # 如果参数function=None,则假定参数function为标识符函数,也就是说,可迭代对象中所有False元素被移除
print(*ft3)

print('---demo04---')
tup2 = (0, False, 11, 22, '', (), [], {})
ft4 = filter(None, tup2)    # 所有False元素被移除
print(ft4)
print(*ft4)



