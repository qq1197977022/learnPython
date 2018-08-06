from collections.abc import Iterable, Iterator

print(isinstance('abc', Iterable))

lst1 = [1, 2, 3, 4]
# next(lst)
# for i in lst1:
#     print(i)

# 列表不是迭代器,但是支持迭代协议,因而可迭代
print('列表: ', f'迭代器:{isinstance(lst1, Iterator)}', f'可迭代{isinstance(lst1, Iterable)}')

f1 = open('a.txt')

print('文件: ', f'迭代器:{isinstance(f1, Iterator)}', f'可迭代{isinstance(f1, Iterable)}')

# for line in f1:
#     print(line)
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

tup1 = (1, 2, 3, 4)
# 元组不是迭代器,但是支持迭代协议,因而可迭代
print('元组: ', f'迭代器:{isinstance(tup1, Iterator)}', f'可迭代{isinstance(tup1, Iterable)}')


print(isinstance(1, object))


gen_iter = (x for x in range(100))
print('生成器迭代器: ', f'迭代器{isinstance(gen_iter, Iterator)}', f'可迭代{isinstance(gen_iter, Iterable)}')

# for语句用于迭代支持序列协议或迭代协议的对象

