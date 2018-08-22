class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def start(self, option):
    #     print(f'{self} {option}')

    def wash(self, good):
        print(f'{self.name} 打开水龙头')
        print(f'{self.name} 洗刷刷 {good}')
        print(f'{self.name} 关闭水龙头')

    # def close(self, option):
    #     print(f'{self} {option}')

    def eat(self, good):
        print(f'{self.name} 吃{good}')


def f():
    ...


if __name__ == '__main__':
    xm = Person(name='小明', age=12, gender='male')
    xm.wash(good='苹果')
    xm.eat(good='苹果')

    print(xm.wash)
    print(f)

