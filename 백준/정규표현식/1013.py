import re 

p = re.compile('(100+1+|01)+')

for i in range(int(input())):
    m = p.fullmatch(input())
    print(m)
    if m :
        print("YES")

    else :
        print("NO")