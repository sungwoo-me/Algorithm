time = [300,60,10]
N = int(input())

result = []
for i in time :
    temp = N // i 
    result.append(temp)
    N=N%i

if N != 0 :
    print(-1)
else :
    print(*result)