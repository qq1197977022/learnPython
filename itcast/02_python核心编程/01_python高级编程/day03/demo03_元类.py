# 类对象默认由默认元类type构造
def print_num(self):
    print(self.num)


# NewClass1的元类即默认元类type
NewClass1 = type("NewClass1", (object,), {'print_num': print_num, 'num': 250})   # 构造一个名字为NewClass1的类
nc1 = NewClass1()
nc1.print_num()
print(NewClass1, nc1, sep='\t')


class NewClass2(object):    # 同上等价
    def __init__(self, num):
        self.num = num

    def print_num(self):
        print(self.num)


nc2 = NewClass2(120)
nc2.print_num()
print(NewClass2, nc2, sep='\t')


print('-' * 60)
print(f'实例对象 nc1的类是{"-"*15}> {nc1.__class__}')
print(f'实例对象 nc2的类是{"-"*15}> {nc2.__class__}')
print(f'类对象 NewClass1的元类是{"-"*9}> {NewClass1.__class__}')
print(f'类对象 NewClass2的元类是{"-"*9}> {NewClass2.__class__}')
print(f'类对象 type的元类是{"-"*14}> {type.__class__}')
print(f'类对象 type的元类的元类是{"-"*9}> {type.__class__.__class__}')









































































