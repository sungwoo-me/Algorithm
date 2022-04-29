T  = int(input())



for i in range(T):
    n=int(input())
    d = [[0,0] for _ in range(41)]
    # 1,2 번쨰 피보나치 수는 1 
    d[0] =[1, 0] 
    d[1] =[0, 1]
    d[2] =[1, 1]
    if n>2 :
        for i in range(3,n+1):
            d[i][0] = d[i-1][0] +d[i-2][0]
            d[i][1] = d[i-1][1] +d[i-2][1]
        
    print(*d[n])



# 피보나치 함수 반복문으로 구현 (바텀업 / 상향식 )


