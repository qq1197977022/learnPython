import re

# demo01. 网址匹配
print(f'{"方式一":-^60}')
s = 'http://interoem.com/messageinfo.asp?id=35' \
    'http://3995503.com/class/class09/news_show.asp?id=14' \
    'http://lib.wzmc.edu.cn/news/onews.asp?id=769' \
    'http://www.zy-ls.com/alfx.asp?newsid=377&id=6' \
    'http://www.fincm.com/newslist.asp?id=415'
p = '(http://.+?)/.*?'  # 为什么这里必须关闭*?贪婪
lst = re.findall(p, s)
print(lst)
print('-'*60)

s = '''
http://interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
p = '(http://.+?)/.*'
lst = re.findall(p, s)  # 而这里不用                 因为前者是多个逻辑行构成的一个行 短字符串, 而后者是多行构成的长字符串    划重点: 前者是单行, 后者是多行,每行后都有一个\n
print(lst)
print('-'*120)


print(f'{"方式二":-^60}')
s = '''
http://interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''


def rep(m_obj):
    return m_obj.group(1)


p = '(http://.+?)/.+'   # 疑问: 为什么关闭贪婪模式, 反而不行?
result_str = re.sub(p, rep, s)
print(result_str)
print('-'*60)


s = 'http://interoem.com/messageinfo.asp?id=35' \
    'http://3995503.com/class/class09/news_show.asp?id=14' \
    'http://lib.wzmc.edu.cn/news/onews.asp?id=769' \
    'http://www.zy-ls.com/alfx.asp?newsid=377&id=6' \
    'http://www.fincm.com/newslist.asp?id=415'


def rep(m_obj):
    print(f'{m_obj.group(1):>30}')
    return m_obj.group(1)


p = '(http://.+?)/.*?'
result_str = re.sub(p, rep, s)
print(result_str)
print('-'*120)


print(f'{"方式三":-^60}')
s = 'http://interoem.com/messageinfo.asp?id=35' \
    'http://3995503.com/class/class09/news_show.asp?id=14' \
    'http://lib.wzmc.edu.cn/news/onews.asp?id=769' \
    'http://www.zy-ls.com/alfx.asp?newsid=377&id=6' \
    'http://www.fincm.com/newslist.asp?id=415'
# s = 'http://interoem.com/messageinfo.asp?id=35'
p = '(http://.+?)/.+?'
result_str = re.sub(p, lambda m_obj: m_obj.group(1), s)
print(result_str)
result_str = re.sub(p, '--->', s)
print(result_str)
p = '(http://.+?)/.+'
result_str = re.sub(p, lambda m_obj: m_obj.group(1), s)
print(result_str)
print('-'*60)


s = '''
http://interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
p = '(http://.+?)/.+'   # 为什么关闭贪婪模式, 反而不行?
result_str = re.sub(p, lambda m_obj: m_obj.group(1), s)
print(result_str)
print('-'*120)


# demo02 找单词
s = 'hello world Ha Ha E-mail _ JetBrains'
# p = '\\b[a-z]*\\b'
p = r'\b[a-zA-Z-]+\b'   # [A-z] == \w == [a-zA-Z0-9_]
lst = re.findall(p, s)
print(lst)

p = ' '
lst = re.split(p, s)
print(lst)



