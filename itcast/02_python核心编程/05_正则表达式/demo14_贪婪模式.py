import re

f = open('file/demo13.html', 'rt', encoding='UTF-8')
contents = f.read()
f.close()

print(f'待处理字符串: \n{contents}')
print('='*120)
p = '<(?:.+)>'  # 数量词* + ?默认贪婪模式, 追加?可关闭贪婪模式
result_str = re.sub(p, '', contents)
print(repr(result_str))
print('='*120)


p = '<(?:.+?)>'  # 关闭贪婪模式
result_str = re.sub(p, '', contents)
print(repr(result_str))
print('='*120)


s = 'This a mumber 234-235-22-423'
p = '.+(\d+-\d+-\d+-\d+)'   # 默认贪婪
m_obj = re.match(p, s)
print(m_obj.groups())
print('='*120)

p = '(.+)(\d+-\d+-\d+-\d+)'
m_obj = re.match(p, s)
print(m_obj.groups())
print('='*120)
# ('This a mumber 23', '4-235-22-423')
# 可以看到贪婪模式下
#   1. .+会尽可能多的匹配字符
#   2. \d+至少一个number

p = '(.+?)(\d+-\d+-\d+-\d+)'  # 关闭贪婪模式
m_obj = re.match(p, s)
print(m_obj.groups())
print('='*120)


s = 'aa2343ddd'
p = 'aa(\d+)'   # 默认贪婪
m_obj = re.match(p, s)
print(m_obj.group(), m_obj.group(1))
print('*'*120)

p = 'aa(\d+?)'  # 关闭贪婪
m_obj = re.match(p, s)
print(m_obj.group(), m_obj.group(1))
print('*'*120)


import re

s = '<img data-original="https://rpic.douyucdn.cn/live-cover/appCovers/2018/04/26/4830538_20180426161215.jpg" ' \
    'src="https://rpic.douyucdn.cn/live-cover/appCovers/2018/04/26/4830538_20180426161215.jpg" ' \
    'style="display: inline;">'
p = 'https://.+\.jpg'   # 数量词* + ?默认贪婪模式
m_obj = re.search(p, s)
if m_obj is not None:
    print(m_obj.group())
else:
    print('-----------')
print('-'*120)

p = 'https://.+?\.jpg'  # 关闭贪婪模式
m_obj = re.search(p, s)
if m_obj is not None:
    print(m_obj.group())
else:
    print('-----------')
print('-'*120)


p = 'https://.+\.jpg'  # 默认贪婪模式
lst = re.findall(p, s)
if lst is not None:
    print(lst)
else:
    print('-----------')
print('-'*120)

p = 'https://.+?\.jpg'  # 关闭贪婪模式
lst = re.findall(p, s)
if lst is not None:
    print(lst)
else:
    print('-----------')
print('-'*120)

































