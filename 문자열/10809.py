from re import I


a= list(input())
b=[]
for i in range(97,123):
    if chr(i) in a :
        b.append(a.index(chr(i)))
    else:
        b.append(-1)

[print(i) for i in b]