# os = __import__('os')
# print(os)
# os.system('calc')
#
#
import sys
# print(dir(sys.modules['builtins']))
# print(dir(sys.modules['builtins']).index('print'))
# num = dir(sys.modules['builtins']).index('print')
# sys.modules['builtins'][num] = input
print(sys.path)
# sys.path = None
# print(sys.path)
import getpass
print(getpass)
p = getpass.getpass('请输入: ')
print(p)



# class D(object):
#     def __gt__(self, other):
#         return True
#
#     def __eq__(self, other):
#         return True
#
#     def __add__(self, other):
#         return 'abc'
#
#
# d1 = D()
# d2 = D()
# print(d1 < d2)
# print(d1 > d2)
# print(d1 == d2)
# print(d1 + d2)
