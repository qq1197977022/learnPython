import re


# 一.边界
#   1.^ $
#   2.\A \Z
#   3.单词边界\b \B
#   Note
#     1.Vim中
#       1.I跳转至行首并进入编辑模式, A跳转至行末并进入编辑模式
#       2.^跳转至行首, $跳转至行末
# 二.分组
#   1.(): 捕获括号
#   2.(?:): 非捕获括号
#   3.\num: 反向引用, 指向指定捕获括号


s = '17513125358'
p = '^1[34578]\d{9}$'
# p = '\A1[34578]\d{9}\Z'
m_obj = re.match(p, s, re.A)
if m_obj is None:
    print(m_obj)
else:
    print(m_obj.group())
print('-'*60)


s = input('请输入一个[0, 100]区间内的数字\n')
# p = '^0$|^100$|^[1-9]0$|^[1-9]{1,2}$'  # 0 ~ 100
# p = '0$|100$|[1-9]\d?$'  # 0 ~ 100
p = '100$|[1-9]?\d?$'  # 0 ~ 100
m_obj = re.match(p, s)
if m_obj is None:
    print(m_obj)
else:
    print(m_obj.group())
print('-'*60)


s = '<html><h1>itcast</h1></html>'
# p = '<(.+)><(.+)>.+</\\2></\\1>'  # 保证标签配对一致
# p = r'<(.+)><(.+)>.+</\2></\1>'   # 原始字符串
p = '<(?P<name1>.+)><(?P<name2>.+)>.+</(?P=name2)></(?P=name1)>'   # 当反向引用较多时, 使用命名法助记
m_obj = re.search(p, s)
if m_obj is None:
    print(m_obj)
else:
    print(m_obj.group(), m_obj.group(0), m_obj.group(1), m_obj.group(2), m_obj.group(1, 2), m_obj.groups(), sep='\n\t')
print('-'*60)


s = '<html><h1>itcast</body></h2>'
p = '<(.+)><(.+)>(.+)</.+></.+>'  # 无法保证标签配对一致
m_obj = re.match(p, s)
if m_obj is None:
    print(m_obj)
else:
    print(m_obj.group(), m_obj.group(0), m_obj.group(1), m_obj.group(2), m_obj.group(1, 2), m_obj.groups(), sep='\n\t')
print('-'*60)


lst = re.findall(p, s)
if lst is None:
    print(lst)
else:
    print(lst)
print('-'*60)


tup = ('1197977022@qq.com', 'Q1197977022@163.cn', '11Q260_Q@gmail.cn', '邮a____@gmail.cn', '_____@gmail.cn', '11Q260_Q@gmail.cnN')
p = '([A-Za-z0-9]\w+)@(163|126|qq|gmail)\.(com|cn|net)$'  # 字母数字开头, [A-z] == \w
for s in tup:
    m_obj = re.match(p, s)  # match方法, 默认从开头开始匹配
    if m_obj is None:
        print(m_obj)
    else:
        print(m_obj.group(), m_obj.groups(), sep='\t')


















































