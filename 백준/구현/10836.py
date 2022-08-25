import sys
input = sys.stdin.readline

M,N = map(int,input().split())



graph= [[1]*M for _ in range(M)]

dx = [-1,-1,0]
dy = [0,-1,-1]







for i in range(N):
    nums = list(map(int,input().split()))
    plus = []
    for j in range(len(nums)):
        for k in range(nums[j]):
            plus.append(j)
    

    num =0     
    for j in range(M-1,-1,-1):
        graph[j][0]=graph[j][0]+ plus[num]
        num +=1 

    for j in range(1,M):
        graph[0][j] = graph[0][j] +plus[num]
        num+=1



    for j in range(1,M):
        for k in range(1,M):
            max = 0 
            for z in range(3):
                nx = j + dx[z]
                ny =k + dy[z]
                if max < graph[nx][ny]:
                    max = graph[nx][ny]
            graph[j][k]=max        
    
for i in graph :
    print(*i)