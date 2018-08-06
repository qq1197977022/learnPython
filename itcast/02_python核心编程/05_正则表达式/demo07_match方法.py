import re
patern = 'abc'
s1 = 'cbaabc'
s2 = 'abccba'
match_obj1 = re.match(patern, s1)   # 仅从开头开始匹配
match_obj2 = re.search(patern, s1)  # 从任意位置开始匹配
print(match_obj1)
if match_obj1 is not None:
    print(match_obj1.group())

print(match_obj2)
if match_obj2 is not None:
    print(match_obj2.group())























