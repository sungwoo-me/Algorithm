def solution(brown, yellow):
    num = brown + yellow 
    nums =[]
    for i in range(3,num+1):
        if num % i == 0:
            j = num // i 
            if 2*(i+j)-4 == brown :
                return [j,i]