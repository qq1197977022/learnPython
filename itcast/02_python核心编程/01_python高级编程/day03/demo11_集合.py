# 集合应用:
#   1.快速成员测试
#   2.序列去重
#   3.数学运算: 1.交集 2.并集 3.差集 4.对称差集

s1 = set('abcA')
s2 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
print('------数学运算------')
print(s1 & s2)    # 交集
print(s1 | s2)    # 并集
print(s1 - s2)    # 差集
print(s1 ^ s2)    # 对称差集 ~ 在A或B中,但不同时在A和B中


str1 = 'aabbccddeeffgg'
tup1 = (1, 1, 2, 2, 'a', 'a', 'b', 'b')
lst1 = [1, 1, 2, 2, 'a', 'a', 'b', 'b']
print('------序列去重------')
print(set(str1))
print(set(tup1))
print(set(lst1))


print('------快速成员测试------')
print('a' in set(str1))
print('a' in set(tup1))
print('a' in set(lst1))
