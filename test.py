N, L , R = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y,num) :
    global sum, cnt ,ok 
    sum+=graph[x][y]
    cnt +=1 
    visited[x][y] = 1
    visited2[x][y] = num
    for a in range(4):
        nx = x+dx[a] 
        ny = y+dy[a]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0  and L<=abs(graph[nx][ny]-graph[x][y]) <=R :
            ok = False
            dfs(nx,ny,num)

    return int(sum/cnt)

graph = []
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
num = 0
nums = []
count = 0

for i in range(N):
    graph.append(list(map(int,input().split())))


while True :
    
    ok = True
    for i in range(N):
        for j in range(N):
            sum = 0
            cnt = 0 
            num+=1 
            if visited[i][j] == 0:
                avg = dfs(i,j,num)

                nums.append([num,avg])

    if ok :
        break
    

    for n,s in nums:
        for i in range(N):
            for j in range(N):
                if visited2[i][j]== n :
                    visited[i][j]=0
                    graph[i][j]=s

    
    count +=1 

print(count)