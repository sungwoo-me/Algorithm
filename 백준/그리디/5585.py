N = int(input())
money = [500,100,50,10,5,1]
N=1000-N
result = 0
for i in money :
    result += N//i
    N=N%i

print(result)