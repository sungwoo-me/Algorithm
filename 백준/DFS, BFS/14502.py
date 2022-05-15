from collections import deque 
from itertools import combinations

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    # 큐 구현을 위해 deque 사용
    que = deque()
    que.append([x,y])
    # 현재 노드를 방문 처리
    visited[x][y]= True
    # 큐가 빌 때 까지 반복 
    while que :
        # 큐에서 하나의 원소를 뽑아 출력하기
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< N and 0<=ny <M and visited[nx][ny] and graph2[nx][ny]==0 :
                visited[nx][ny] = False
                graph2[nx][ny] = 2
                que.append([nx,ny])


def countvw():
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 2 :
                virus.append([i,j])
            elif graph[i][j] == 0 :
                wall.append([i,j])
    return

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
virus = []
wall = []
result = []
countvw()

wall = list(combinations(wall,3))

for i in wall :
    graph2 = [[r for r in q ] for q in graph]
    visited  = [[True]*M for _ in range(N)]
    for j in i :
        x,y= j 
        graph2[x][y] = 1 
    
    for k in virus :
        x,y = k 
        bfs(x,y)    

    cnt = 0 
    for h in graph2 :
        for y in h :
            if y == 0 :
                cnt+=1 

    result.append(cnt)

print(max(result))
    
