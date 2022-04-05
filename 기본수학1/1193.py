n = int (input())

i= 1

while True :
    if i>=n:
        break;
    n=n-i
    i+=1



result=[str(n),"/",str(i-n+1)]

if i%2==1:
    result.reverse()
    [print(i ,end='') for i in result]

else :
    [print(i,end='') for i in result]


"""
11
12 21
31 22 13
14 23 32 41
51 42 33 24 15
16 25 34 43 52 61
71 62 53 44 35 26 17
18 27 36 45 54 63 72 81



""" 