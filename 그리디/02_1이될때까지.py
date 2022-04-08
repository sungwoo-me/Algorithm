import re


N, K = map(int,input().split())




result =0 

while True:
    # N 이 K 로 나누어 떨어지는 수가 될 떄 까지 1 씩 빼기

    if N == 1 :
        break
    if N%K == 0:
        N=N/K
    else :
        N-K

    result +=1
    
print(result)