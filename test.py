# import hashlib
# sha1 = hashlib.new('sha1')      # 密文存储
# sha1.update('123'.encode())
# password = sha1.hexdigest()
# print(password)
#
# # 123: 40bd001563085fc35165329ea1ff5c5ecbdbbeef: 9adcb29710e807607b683f62e555c22dc5659713: 这样只需要记住原始密码123和加密规则,
# # 即可完成不可破解加密, 因为这种加密规则是私人算法
#
#
# m = hashlib.sha1()
# m.update('123'.encode())
# r = m.hexdigest()
# print(r)
from datetime import date
print(date.today())


class Person(object):
    name = '张三'
    age = 3

    def say(self):
        print(self.name, self.age)


p = Person()
p.say()

p.name = '李四'
p.say()



























