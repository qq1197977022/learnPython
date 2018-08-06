def f1():   # 选择结构
    pass
    # if 2 > 1:
    #     print('2大于1')

    # if 2 > 1:
    #     print('2大于1')
    # else:
    #     print('1大于2')

    # if 2 > 1:
    #     print('2大于1')
    # elif 1 > 2:
    #     print('1大于2')
    # else:
    #     print('1等于2')

    # print(1)
    # print(2)
    # print(3)


def f2():
    # str1 = 'ABCDE'
    # for ele in str1:
    #     print(ele)
    # str2 = '12345'
    # for ele in str2:
    #     print(ele)
    str3 = '核桃编程教育'
    for ele in str3:
        print(ele)


def f3():
    # 1.迭代序列
    # lst1 = [1, 2, 'A', 'B', '核桃', '少儿编程']
    # tup1 = (1, 2, 'A', 'B', '核桃', '少儿编程')
    # dic1 = {'name': 'xxx', 'age': 22, 'gender': 'male'}
    # for k, v in dic1.items():
    #     print(k, v)

    # 2.迭代可迭代对象
    f = open('demo0x_控制流程.py', encoding='utf-8')
    for line in f:
        print(line)


def f4():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{j}*{i}={i*j}\t', end='')
        print()


if __name__ == '__main__':
    pass
    # f1()
    # f2()
    # f3()
    f4()
