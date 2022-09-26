import re 

# 1. match (일치하는거 찾기)

# compile 옵션
# re.I : 대소문자 무시 
# re.M : 여러 줄 한번에 검사
# r'string' : /나오면 써주기 
# ^  : 맨처음 나오는지
# \s : 문장 중간에 나올 수 있는 공백 
# \w : word 단어가 반복 
# |  : or 
# ^  : 
# $  : 맨끝에 나오는지 
# \b : 문자 끝에 나오는 공백

# 그루핑 () : ABC 반복을 찾고 싶으면 (ABC)묶어주고 사용 
# sub('a','b') : a 일치 있으면 b 로 바꿔라 

p = re.compile('[a-z]+')
m = p.match('python 3')
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
