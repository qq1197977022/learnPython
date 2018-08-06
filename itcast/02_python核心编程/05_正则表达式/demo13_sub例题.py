import re

f = open('file/demo13.html', 'rt', encoding='UTF-8')
contents = f.read()
f.close()

p = '<p>(.*)</p>'
lst = re.findall(p, contents)
for i, v in enumerate(lst):
    print(i, v, sep='\t')
print('-'*60)


# 一.去掉标签括号
s = re.sub('<.+>', '', contents)    # 数量词* + ?默认贪婪模式, 追加?可关闭贪婪模式
print(repr(s))
print('-'*60)


s = re.sub('<(?:/?\w+)>', '', contents)
print(s)
print('-'*60)

tup = re.subn('<(?:/?\w+)>', '', contents)
print(tup)
for i in tup:
    print(i)
print('-'*60)

s = 'python, java-cpp &C++ (PHP'
p = ',| |-|&|\('
lst = re.split(p, s)
print(lst)
print('-'*60)
































