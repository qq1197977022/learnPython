print(1, 2, 3,
      4, 5)


a, b, c, d = 1, 3, \
             4,\
             5
print(a, b, c, d)


a1, a2, a3, a4 = (1, 2,
                  4, 5)
print(a1, a2, a3, a4)


str1 = 'abcdefgh' \
       'ijkmln'


def f(
        arg1,
        arg2,
        arg3, arg4):
    print(arg1, arg2, arg3, arg4)


f(1, 2, 3, 4)

if (1 < 2 and 3 < 4):    # 不换行加括号,但会提示redundant parentheses冗余括号
    pass

if (1 < 2    # 换行加括号,有利于代码分块,此时的括号不是冗余的
        and 3 < 4):
    print(333)


# if 1 < 2 and \    # 不加括号,使用显式行连接规则 ~ 不能包含注释
#         3 < 4:
#     print(444)

if 1 < 2 \
        and 3 < 4:
    print(444)


lst = [
    1, 2, 3,
    4, 5, 6
]


if 3 < 4: print('222'); print('333')    # 在当前上下文,分号比冒号绑定更紧密










































