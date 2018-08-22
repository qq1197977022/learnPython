class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name}会吃东西, 但吃什么不确定')


class Cat(Animal):
    def __init__(self, name, hobby):
        super(Cat, self).__init__(name)
        self.hobby = hobby

    # 重写父类方法
    def eat(self):
        print(f'{self.name}吃{self.hobby}')

    def climb(self):
        print(f'{self.name}会爬树')


if __name__ == '__main__':
    animal = Animal('动物')
    animal.eat()

    cat = Cat('橘猫', '老鼠')
    cat.eat()   # 继承 or 重写
    cat.climb()



