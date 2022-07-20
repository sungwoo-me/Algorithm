from collections import deque

def bfs(x,y):
    que = deque()
    que.append([x,y,0])
    visited[x][y] = False
    while que : 
        x,y,count = que.popleft()

        if [x,y] in store:
            count = 0
        
        if [x,y] == finish :
            return "happy"
        
        count +=1       

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=finish[0] and 0<=ny<=finish[1] and visited[nx][ny] and count <=1000 :
                que.append([nx,ny,count])
                visited[nx][ny] = False

    
    return "sad"


T = int(input())
for i in range(T):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    N = int(input())
    home = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(N)]
    finish = list(map(int,input().split()))
    
    visited = [[True]*(finish[1]+1) for _ in range((finish[0]+1))]

    print(bfs(home[0],home[1]))
