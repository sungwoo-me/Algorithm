dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
for i in input():
    for j in dial:
        if i in j:
            sum += dial.index(j)+3
print(sum)