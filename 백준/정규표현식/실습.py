import re 

# 1. match (일치하는거 찾기)

p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print("---------")

# 2. search (그안에 매치되는게 그 문장만 있으면 리턴)

p2 = re.compile('[a-z]+')
m2 = p2.search('3 python')
print(m2)
print("---------")

# 3. findall (일치하는 스트링을 리스트로 리턴)

p3 = re.compile('[a-z]+')
m3 = p3.findall('life is too short')
print(m3)
print("---------")
