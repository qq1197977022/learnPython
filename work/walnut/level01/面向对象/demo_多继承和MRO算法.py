class A(object):
    def smile(self):
        print('smile...A...')


class B(A):
    def smile(self):
        print('smile...B...')

    def cry(self):
        print('cry...B...')


class C(A):
    def cry(self):
        print('cry...C...')

    def run(self):
        print('run...D...')


# class D(B, C):
class D(C, B):
    pass


if __name__ == '__main__':
    d = D()
    d.smile()
    d.cry()
    d.run()

