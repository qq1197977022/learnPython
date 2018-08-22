class A(object):
    def __init__(self, name):
        self.name = name

    def eat_apple(self):
        print(f'{self.name}会吃苹果')

    # def cry(self):
    #     print('cry...A...')


class B(object):
    def __init__(self, name):
        self.name = name

    def eat_bear(self):
        print(f'{self.name}会吃梨')

    # def cry(self):
    #     print('cry...B...')


class C(A, B):
    def eat(self):
        self.eat_apple()
        self.eat_bear()

    def run(self):
        print(f'{self.name}会跑')


if __name__ == '__main__':
    a = A('A 同学')
    b = B('B 同学')
    c = C('C 同学')

    a.eat_apple()
    b.eat_bear()
    print('-'*50)
    c.eat()
    print('-'*50)
    c.eat_apple()
    c.eat_bear()
    c.run()

    # c.cry()
