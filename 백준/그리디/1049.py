N, M  = map(int,input().split())
price = [[0,0] for _ in range(M)]
min_one = 1000
min_six = 1000
for i in range(M):
    a,b=map(int,input().split())
    if a < min_six :
        min_six = a
    if b < min_one : 
        min_one = b 
    if b*6 < min_six :
        min_six = b*6



six = N//6 
one = N%6

if one*min_one <= min_six :    
    print(min_one*one + min_six*six)

else :
    print(min_six*(six+1))

