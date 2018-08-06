import types


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}在吃饭')


def run(self):
    print(f'{self.name}年龄为{self.age}--->会跑步...')


p1 = Person("p1", 18)
p1.eat()

# 给实例对象添加数据属性
print('---' * 60, '添加数据属性')
p1.addr = "河南-郑州-金水区"
print(p1.addr)

# 给实例对象添加函数
print('---' * 60, '添加函数')
p1.run = run
print(p1.run, p1.eat, sep='\t')
p1.run(p1)    # 方法的本质

# 给实例对象添加方法
print('---' * 60, '添加方法')
p1.run = types.MethodType(run, p1)    # 返回绑定到p1对象的方法对象的引用
print(p1.run, p1.eat, sep='\t')
p1.run()

# 用装饰器实现
print('---' * 60, '用装饰器假模拟types.MethodType()')
def f(fun, ins):
    def inner():
        fun(ins)
    return inner


p1.run = f(run, p1)
print(p1.run)
p1.run()
