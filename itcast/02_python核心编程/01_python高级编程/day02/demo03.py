class Reverse(object):
    '''逆序迭代器'''
    def __init__(self, data):
        print('自定义初始化: ', '-' * 30)
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print('迭代器: ', '+' * 30)
        return self

    def __next__(self):
        print('开始迭代: ', '=' * 30)
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse('abcdefg')
print(rev)

it = iter(rev)
print(it)

# for i in it:
#     print(i)

ele = next(it)
print(ele)


#   1.python支持容器上的迭代概念
#       1.容器需要定义__iter__()方法以支持迭代

#   2.迭代器
#       1.迭代器必须实现__iter__()和__next__()方法,因为它们构成迭代器协议


lst1 = [1, 2, 3]
tup1 = (1, 2, 3)
dic1 = {1: 'a', 2: 'b', 3: 'c'}
str1 = 'abc'
f1 = open('a.txt')

# 可迭代对象,支持解压操作
print(f'列表: {lst1}\t', *lst1)
print(f'元组: {tup1}\t', *tup1)
print(f'字符串: {str1}\t', *str1)
print(f'字典: {dic1}\t', *dic1)
print(f'文件: {f1}\t', *f1)

