class A(object):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print(f'{self.name}哭了...555...')


class B(object):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print(f'{self.name}哭了...呜呜呜...')


def obj_cry(obj):
    obj.cry()


def main():
    a = A('A 同学')
    b = B('B 同学')
    obj_cry(a)
    obj_cry(b)


if __name__ == '__main__':
    main()

