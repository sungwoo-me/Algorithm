import re

# (10 0 ~ 1~  or 01 ) ~ 
# 100 뒤에 0 자유 1 뒤에 1 자유  or 01  이게 반복 !! 

p = re.compile('(100+1+|01)+')
m = p.fullmatch(input())

if m : 
    print("SUBMARINE")
else :
    print("NOISE")
