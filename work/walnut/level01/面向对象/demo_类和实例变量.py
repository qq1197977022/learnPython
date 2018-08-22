class Person(object):
    appleList = ['oneApple', 'twoApple', 'threeApple']

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.name}\t {self.age}\t {self.gender}'

    def eat(self, fruit):
        self.appleList[0] = fruit


if __name__ == '__main__':
    # 实例化Person类
    tom = Person(name='汤姆', age=12, gender='male')
    jerry = Person(name='杰瑞', age=13, gender='female')

    print(tom)
    print(jerry)
    print('-'*15)
    # 修改实例对象tom的数据属性age
    tom.age += tom.age
    print(tom)
    print(jerry)
    print('-'*15)
    # 实例对象共享类的属性
    print(tom.appleList)
    print(jerry.appleList)
    print(Person.appleList)
    print('-'*15)
    # tom想吃苹果, 拿梨换苹果
    tom.eat(fruit='bear')
    print(tom.appleList)
    print(jerry.appleList)

