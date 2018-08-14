def f0():
    print(1)
    print(2)
    print(3)


def f1():   # 选择结构
    pass
    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))
    # 两路分支
    if num1 > num2:
        print(f'{num1} > {num2}')
    else:
        print(f'{num2} > {num1}')
    # 多路分支
    if num1 > num2:
        print(f'{num1} > {num2}')
    elif num1 < num2:
        print(f'{num1} < {num2}')
    else:
        print(f'{num1} = {num2}')


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
        else:
            print()


def f5():
    # for i in range(3):
    #     print(i)
    # else:
    #     print('over')

    # for i in range(5):
    #     if i == 3:
    #         break
    #     print(i)
    # else:
    #     print('over...')

    # for i in range(5):
    #     if i == 3:
    #         continue
    #     print(i)
    # else:
    #     print('over...')

    # break和continue关键字
    for i in range(5):
        if i == 4:
            continue
        print(i)
    else:
        print('------over------')


def f6():
    pass
    for i in range(0, 5, 2):
        print(i)


if __name__ == '__main__':
    # f0()
    f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
