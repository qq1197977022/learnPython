import re


print('-'*60)
s = '\\nabc'
p = '\\\\n[a-z]+'
match_obj = re.match(p, s)
print(p, match_obj)


print('-'*60)
s = '\\nabc'
p = '\\\\n[a-z]+'
# p = r'\\n[a-z]+'    # 原始字符串   ~ 避免转义
match_obj = re.match(p, s)
print(p, match_obj)


print('-'*60)
s = '\nabc'
p = '\s[a-z]+'
match_obj = re.match(p, s)
print(p, match_obj)


print('-'*60)
s = 'abc\nabc'
p = '[a-z]*\s[a-z]*'
match_obj = re.search(p, s)
print(p, match_obj)
print(match_obj.group())
print(repr(match_obj.group()))





















