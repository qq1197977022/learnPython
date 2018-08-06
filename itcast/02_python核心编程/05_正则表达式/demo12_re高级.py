import re

# match()
# search()
# findall()


# 匹配替换
s = 'python=50, php=0, java=100, C=998 998'
p = '\d+'
rest_str = re.sub(p, '520', s)  # 默认全部替换
print(rest_str, '-'*60, sep='\n')

rest_str = re.sub(p, '520', s, 1)
print(rest_str, '-'*60, sep='\n')

rest_str = re.sub(p, '520', s, 2)
print(rest_str, '-'*60, sep='\n')


def add100(m_obj):
    return f'{int(m_obj.group()) + 100}'


rest_str = re.sub(p, add100, s)  # 使用替换函数
print(rest_str, '-'*60, sep='\n')









































