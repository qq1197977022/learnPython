class A(object):
    def __getattribute__(self, item):
        if item == 'attr1':
            return '牛逼...'
        else:
            print('-----'*30)
            ret = self.f1
            print('+++++' * 30)
            return ret

    def f1(self):
        print('我曹?')

    def f2(self):
        self.f2()


a = A()
print(a.attr1)    # 野属性 ~ 本座提名!
# print(a.attr2)    # 无限递归
# a.f2()    # 无限递归

