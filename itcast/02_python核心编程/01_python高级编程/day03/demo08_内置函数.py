def f1(arg1, arg2):
    print(f'{"函数被调用":-^60}')
    return arg1+arg2


tup_num = (1, 2, 3, 4, 5)
lst_num = range(1, 6)

m1 = map(f1, tup_num, lst_num)

# print(m1)
# print(*m1)
# print(**m1)    # TypeError: print() argument after ** must be a mapping, not map


#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#
#                   1.map()函数返回的是一个迭代器对象map
#                   2.map和mapping是两个不同的对象 ~ mapping是存储键值对的字典dict
#
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#                   Note!...Note!...Note!...Note!...Note!...Note!...Note!...Note!...
#

print(*m1)


m2 = map(lambda x, y: x*y, tup_num, lst_num)
print(*m2)














































